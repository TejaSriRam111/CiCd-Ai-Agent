import sys
sys.stdout.reconfigure(encoding="utf-8")
from agent.cicd_agent import CICDAgent
from llm.ollama_llm import ask_ollama
from utils.git_utils import resolve_repo

def main():
    print("CI/CD AI Agent Started")

    repo_url = input("Enter Git repository URL: ").strip()
    if not repo_url:
        print("Repository URL cannot be empty")
        return

    repo_path = resolve_repo(repo_url)

    agent = CICDAgent(llm=ask_ollama)
    agent.run(repo_path, mode="full-devops")

if __name__ == "__main__":
    main()
