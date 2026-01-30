import os

def write_workflow(repo_path, yaml_content):
    path = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, "ci-cd.yml"), "w") as f:
        f.write(yaml_content)
