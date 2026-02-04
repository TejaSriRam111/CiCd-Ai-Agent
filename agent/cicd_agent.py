from analyzer.repo_analyzer import analyze_repo
from agent.planner import plan_pipeline
from generator.workflow_writer import write_workflow
from utils.git_utils import commit_and_push


class CICDAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, repo_path, mode="full-devops"):
        # Analyze the repository
        repo_context = analyze_repo(repo_path)

        # Generate CI/CD pipeline using LLM
        workflow_yaml = plan_pipeline(repo_context, self.llm, mode)

        # Write the workflow file into the target repo
        write_workflow(repo_path, workflow_yaml)

        # Automatically commit and push the workflow
        commit_and_push(repo_path)

        print("CI/CD generated and pushed to repository")
