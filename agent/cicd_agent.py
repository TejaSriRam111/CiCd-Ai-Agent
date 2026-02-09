from analyzer.repo_analyzer import analyze_repo
from agent.planner import plan_pipeline
from generator.workflow_writer import write_workflow
from utils.git_utils import commit_and_push


class CICDAgent:
    def __init__(self, llm=None):
        self.llm = llm

    def run(self, repo_path, mode="full-devops"):
        print("Analyzing repository...")
        repo_context = analyze_repo(repo_path)

        print("Planning CI/CD pipeline...")
        workflow_plan = plan_pipeline(repo_context, self.llm, mode)

        print("Writing CI/CD workflow...")
        write_workflow(repo_path, workflow_plan)

        print("Committing & pushing workflow...")
        commit_and_push(repo_path)

        print("CI/CD workflow generated, committed, and pushed successfully")
