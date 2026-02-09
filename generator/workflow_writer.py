import os

FORBIDDEN_PATTERNS = [
    "working-dir",
    "working_directory",
    "continue:",
    "azure/login",
    "appleboy",
    "exists(",
    "if:",
    "node-version: 14",
    "actions/setup-node@v2",
    "actions/setup-node@v3"
]


def strip_non_yaml(text):
    lines = text.splitlines()
    cleaned = []
    started = False

    for line in lines:
        if line.strip().startswith("```"):
            continue
        if not started:
            if line.strip().startswith("name:"):
                started = True
                cleaned.append(line)
        else:
            cleaned.append(line)

    return "\n".join(cleaned)


def normalize_yaml(yaml_text):
    if "on: [push]" in yaml_text:
        yaml_text = yaml_text.replace(
            "on: [push]",
            "on:\n  push:\n    branches:\n      - main"
        )

    if "on:" not in yaml_text:
        yaml_text = yaml_text.replace(
            "name:",
            "name:\n\non:\n  push:\n    branches:\n      - main\n"
        )

    return yaml_text


def ensure_steps(yaml_text):
    lines = yaml_text.splitlines()
    fixed = []

    i = 0
    while i < len(lines):
        line = lines[i]
        fixed.append(line)

        if line.strip() == "steps:":
            j = i + 1
            has_step = False
            while j < len(lines):
                nxt = lines[j].strip()
                if nxt == "" or nxt.startswith("#"):
                    j += 1
                    continue
                if nxt.startswith("-"):
                    has_step = True
                break

            if not has_step:
                indent = line[:len(line) - len(line.lstrip())]
                fixed.append(f"{indent}- uses: actions/checkout@v4")

        i += 1

    return "\n".join(fixed)


def validate_yaml(yaml_text):
    for bad in FORBIDDEN_PATTERNS:
        if bad in yaml_text:
            raise ValueError(f"Invalid GitHub Actions syntax detected: {bad}")

    if not yaml_text.strip().startswith("name:"):
        raise ValueError("Workflow must start with 'name:'")

    if "run:" not in yaml_text:
        raise ValueError("Workflow must contain run steps")


def write_workflow(repo_path, yaml_content):
    workflow_dir = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_file = os.path.join(workflow_dir, "ci-cd.yml")

    yaml_text = strip_non_yaml(yaml_content)
    yaml_text = normalize_yaml(yaml_text)
    yaml_text = ensure_steps(yaml_text)
    validate_yaml(yaml_text)

    with open(workflow_file, "w", encoding="utf-8", newline="\n") as f:
        f.write(yaml_text)
