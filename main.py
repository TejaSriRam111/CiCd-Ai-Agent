from agent.cicd_agent import CICDAgent
from llm.claude import ask_claude
from tools.repo_resolver import resolve_repo

def main():
    print("🤖 CI/CD AI Agent Started")
    
    repo_url = input("👉 Enter Git repository URL: ").strip()
    if not repo_url:
        print("❌ Repo URL cannot be empty")
        return

    repo_path = resolve_repo(repo_url)

    agent = CICDAgent(llm=ask_claude)
    agent.run(repo_path, mode="full-devops")

if __name__ == "__main__":
    main()
