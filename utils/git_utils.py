import os
import subprocess
from urllib.parse import urlparse

CLONE_ROOT = "cloned_repos"


def resolve_repo(repo_url: str) -> str:
    """
    Takes a git repo URL or local path and returns a local repo path
    """

    # Local path
    if os.path.exists(repo_url):
        return repo_url

    # Git URL
    if repo_url.startswith("http"):
        parsed = urlparse(repo_url)
        repo_name = parsed.path.strip("/").split("/")[-1].replace(".git", "")
        clone_dir = os.path.join(CLONE_ROOT, repo_name)

        os.makedirs(CLONE_ROOT, exist_ok=True)

        if not os.path.exists(clone_dir):
            print(f"Cloning repository: {repo_url}")
            subprocess.run(
                ["git", "clone", repo_url, clone_dir],
                check=True
            )
        else:
            print("Repository already cloned")

        return clone_dir

    raise ValueError("Invalid repository URL or path")


def commit_and_push(
    repo_path: str,
    message: str = "Add AI-generated CI/CD pipeline"
):
    """
    Commits and pushes the generated CI/CD workflow to the target repository
    """

    workflow_path = os.path.join(".github", "workflows", "ci-cd.yml")

    if not os.path.isdir(os.path.join(repo_path, ".git")):
        print("Not a git repository, skipping commit")
        return

    full_workflow_path = os.path.join(repo_path, workflow_path)

    if not os.path.exists(full_workflow_path):
        print("No CI/CD workflow found to commit")
        return

    try:
        def run(cmd):
            subprocess.run(cmd, cwd=repo_path, check=True)

        # Ensure git identity exists
        run(["git", "config", "user.email", "ai-agent@github.com"])
        run(["git", "config", "user.name", "CI/CD AI Agent"])

        # Stage workflow
        run(["git", "add", workflow_path])

        # Check if there are changes
        status = subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=repo_path
        ).decode().strip()

        if not status:
            print("No changes to commit")
            return

        # Commit and push
        run(["git", "commit", "-m", message])
        run(["git", "push"])

        print("CI/CD workflow committed and pushed successfully")

    except subprocess.CalledProcessError as e:
        print("Git commit or push failed")
        raise e
