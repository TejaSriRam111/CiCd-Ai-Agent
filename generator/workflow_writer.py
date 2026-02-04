import os


def normalize_github_actions_yaml(yaml_text: str) -> str:
    """
    Fix common LLM mistakes in GitHub Actions YAML
    """

    # Fix invalid short-form trigger
    if "on: [push]" in yaml_text:
        yaml_text = yaml_text.replace(
            "on: [push]",
            "on:\n  push:\n    branches:\n      - main"
        )

    # Remove standalone branches (invalid placement)
    lines = yaml_text.splitlines()
    cleaned = []
    skip_branches_block = False

    for line in lines:
        if line.strip() == "branches:":
            skip_branches_block = True
            continue
        if skip_branches_block:
            if line.startswith(" ") or line.startswith("-"):
                continue
            else:
                skip_branches_block = False
        cleaned.append(line)

    return "\n".join(cleaned)


def write_workflow(repo_path, yaml_content):
    workflow_dir = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_file = os.path.join(workflow_dir, "ci-cd.yml")

    # ---- SANITIZE LLM OUTPUT ----
    lines = yaml_content.splitlines()

    cleaned_lines = []
    yaml_started = False

    for line in lines:
        # Skip markdown fences
        if line.strip().startswith("```"):
            continue

        # Start only from first 'name:'
        if not yaml_started:
            if line.strip().startswith("name:"):
                yaml_started = True
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)

    cleaned_yaml = "\n".join(cleaned_lines)

    # ---- NORMALIZE GITHUB ACTIONS SYNTAX ----
    cleaned_yaml = normalize_github_actions_yaml(cleaned_yaml)

    with open(workflow_file, "w", encoding="utf-8") as f:
        f.write(cleaned_yaml)
