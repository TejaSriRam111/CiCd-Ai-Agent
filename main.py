from utils.git_utils import clone_repo
from analyzer.repo_analyzer import analyze_repo
from generator.github_actions import generate_pipeline
import os

def main():
    repo_url = input("Enter GitHub repo URL: ")

    repo_path = clone_repo(repo_url)
    tech = analyze_repo(repo_path)

    print("\nDetected Tech Stack:")
    print(tech)

    pipeline_yaml = generate_pipeline(tech)

    os.makedirs(".github/workflows", exist_ok=True)

    with open(".github/workflows/ci.yml", "w") as f:
        f.write(pipeline_yaml)

    print("\nCI/CD pipeline generated at .github/workflows/ci.yml")

if __name__ == "__main__":
    main()
