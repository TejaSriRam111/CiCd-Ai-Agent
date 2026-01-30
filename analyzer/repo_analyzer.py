import os

DEPLOY_FILES = [
    "Dockerfile",
    "docker-compose.yml",
    "vercel.json",
    "netlify.toml",
    "firebase.json"
]

def analyze_repo(repo_path):
    files = os.listdir(repo_path)

    return {
        "files": files,
        "deployable": any(f in files for f in DEPLOY_FILES),
        "has_docker": "Dockerfile" in files
    }
