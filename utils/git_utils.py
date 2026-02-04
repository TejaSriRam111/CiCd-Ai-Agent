import os
import subprocess
from urllib.parse import urlparse

CLONE_ROOT = "cloned_repos"

def resolve_repo(repo_url: str) -> str:
    """
    Takes a git repo URL or local path and returns a local repo path
    """

    # If local path already exists
    if os.path.exists(repo_url):
        return repo_url

    # If Git URL
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


def commit_and_push(repo_path: str, message: str = "Add AI-generated CI/CD pipeline"):
    """
    Commits and pushes the generated CI/CD workflow to the target repository
    """

    workflow_path = os.path.join(".github", "workflows", "ci-cd.yml")

    try:
        # Ensure workflow exists before committing
        if not os.path.exists(os.path.join(repo_path, workflow_path)):
            print("No CI/CD workflow found to commit")
            return

        subprocess.run(
            ["git", "add", workflow_path],
            cwd=repo_path,
            check=True
        )

        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=repo_path,
            check=True
        )

        subprocess.run(
            ["git", "push"],
            cwd=repo_path,
            check=True
        )

        print("CI/CD workflow committed and pushed successfully")

    except subprocess.CalledProcessError as e:
        print("Git commit or push failed")
        print(e)
