import os


def write_workflow(repo_path, plan):
    # Safety check
    if not isinstance(plan, dict):
        raise ValueError("Workflow plan must be a dictionary")

    deploy_dir = plan.get("deploy_dir", "build")
    language = plan.get("language", "unknown")
    build_command = plan.get("build_command", "echo Build step")

    workflow_dir = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_file = os.path.join(workflow_dir, "ci-cd.yml")

    workflow_content = f"""
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Setup Environment
        run: echo "Setting up for {language}"

      - name: Build Step
        run: {build_command}

      - name: Deploy Step
        run: echo "Deploying from {deploy_dir}"
"""

    with open(workflow_file, "w", encoding="utf-8") as f:
        f.write(workflow_content)

    print("CI/CD workflow file created successfully.")
