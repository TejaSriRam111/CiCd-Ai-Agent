from utils.git_utils import clone_repo
from analyzer.repo_analyzer import analyze_repo
from generator.github_actions import generate_pipeline
import os

def main():
    repo_url = input("Enter GitHub repo URL: ").strip()

    # 1. Clone target repo
    repo_path = clone_repo(repo_url)

    # 2. Analyze cloned repo
    tech = analyze_repo(repo_path)

    print("\nDetected Tech Stack:")
    print(tech)

    # 3. Generate pipeline YAML
    pipeline_yaml = generate_pipeline(tech)

    # 4. Create workflows directory INSIDE THE CLONED REPO
    workflows_dir = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(workflows_dir, exist_ok=True)

    # 5. Write ci.yml INSIDE THE CLONED REPO
    ci_file_path = os.path.join(workflows_dir, "ci.yml")
    with open(ci_file_path, "w", encoding="utf-8") as f:
        f.write(pipeline_yaml)

    print(f"\nCI/CD pipeline generated INSIDE repo at:")
    print(ci_file_path)

if __name__ == "__main__":
    main()
