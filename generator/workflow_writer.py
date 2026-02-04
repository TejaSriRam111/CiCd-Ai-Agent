import os

def write_workflow(repo_path, yaml_content):
    workflow_dir = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_file = os.path.join(workflow_dir, "ci-cd.yml")

    # --- SANITIZE LLM OUTPUT ---
    lines = yaml_content.splitlines()

    cleaned_lines = []
    yaml_started = False

    for line in lines:
        # Skip markdown fences and explanations
        if line.strip().startswith("```"):
            continue
        if not yaml_started:
            if line.strip().startswith("name:"):
                yaml_started = True
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)

    cleaned_yaml = "\n".join(cleaned_lines)

    with open(workflow_file, "w", encoding="utf-8") as f:
        f.write(cleaned_yaml)
