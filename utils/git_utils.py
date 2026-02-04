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
