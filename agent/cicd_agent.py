from analyzer.repo_analyzer import analyze_repo
from agent.planner import plan_pipeline
from generator.workflow_writer import write_workflow


class CICDAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, repo_path, mode="full-devops"):
        repo_context = analyze_repo(repo_path)
        workflow_yaml = plan_pipeline(repo_context, self.llm, mode)
        write_workflow(repo_path, workflow_yaml)
        print("CI/CD workflow generated and validated")
