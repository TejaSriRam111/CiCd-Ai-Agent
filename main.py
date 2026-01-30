from agent.cicd_agent import CICDAgent
from llm.claude import ask_claude

def main():
    agent = CICDAgent(llm=ask_claude)
    agent.run("./target-repo", mode="full-devops")

if __name__ == "__main__":
    main()
