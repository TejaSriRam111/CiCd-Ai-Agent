import sys
from agent.cicd_agent import CICDAgent
from llm.claude import ask_claude

def main():
    repo_path = sys.argv[1]
    agent = CICDAgent(llm=ask_claude)
    agent.run(repo_path, mode="full-devops")

if __name__ == "__main__":
    main()
