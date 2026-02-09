import os


def ensure_minimum_steps(yaml_text: str) -> str:
    """
    Ensure every job has at least one valid step.
    Fixes empty 'steps:' blocks which break GitHub Actions.
    """

    lines = yaml_text.splitlines()
    fixed_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        fixed_lines.append(line)

        if line.strip() == "steps:":
            j = i + 1
            has_step = False

            while j < len(lines):
                next_line = lines[j].strip()
                if next_line == "" or next_line.startswith("#"):
                    j += 1
                    continue
                if next_line.startswith("-"):
                    has_step = True
                break

            if not has_step:
                indent = line[:len(line) - len(line.lstrip())]
                fixed_lines.append(f"{indent}- uses: actions/checkout@v4")

        i += 1

    return "\n".join(fixed_lines)


def normalize_github_actions_yaml(yaml_text: str) -> str:
    """
    Fix common LLM GitHub Actions mistakes.
    """

    # Fix invalid short trigger
    if "on: [push]" in yaml_text:
        yaml_text = yaml_text.replace(
            "on: [push]",
            "on:\n  push:\n    branches:\n      - main"
        )

    # Ensure 'on:' exists
    if "on:" not in yaml_text:
        yaml_text = yaml_text.replace(
            "name:",
            "name:\n\non:\n  push:\n    branches:\n      - main\n"
        )

    return yaml_text


def strip_non_yaml_content(yaml_content: str) -> str:
    """
    Strip markdown, explanations, and anything before the YAML starts.
    """

    lines = yaml_content.splitlines()
    cleaned_lines = []
    yaml_started = False

    for line in lines:
        if line.strip().startswith("```"):
            continue

        if not yaml_started:
            if line.strip().startswith("name:"):
                yaml_started = True
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def write_workflow(repo_path, yaml_content):
    workflow_dir = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_file = os.path.join(workflow_dir, "ci-cd.yml")

    # 1️⃣ Strip non-YAML junk
    cleaned_yaml = strip_non_yaml_content(yaml_content)

    # 2️⃣ Normalize known GitHub Actions issues
    cleaned_yaml = normalize_github_actions_yaml(cleaned_yaml)

    # 3️⃣ Ensure no empty steps blocks
    cleaned_yaml = ensure_minimum_steps(cleaned_yaml)

    # 4️⃣ Final safety check
    if not cleaned_yaml.strip().startswith("name:"):
        raise ValueError("Invalid workflow: YAML does not start with 'name:'")

    with open(workflow_file, "w", encoding="utf-8", newline="\n") as f:
        f.write(cleaned_yaml)
