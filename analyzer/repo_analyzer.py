import os
import json


def analyze_repo(repo_path):
    files = os.listdir(repo_path)

    package_json_path = os.path.join(repo_path, "package.json")

    has_package_json = os.path.exists(package_json_path)
    has_docker = "Dockerfile" in files

    has_build_dir = os.path.isdir(os.path.join(repo_path, "build"))
    has_dist_dir = os.path.isdir(os.path.join(repo_path, "dist"))

    is_static_site = any(
        f.endswith(".html") for f in files
    )

    # Detect required Node version (default to 20)
    node_version_required = "20"
    if has_package_json:
        try:
            with open(package_json_path, "r", encoding="utf-8") as f:
                pkg = json.load(f)
                engines = pkg.get("engines", {})
                if "node" in engines:
                    node_version_required = engines["node"]
        except Exception:
            pass  # Fail safe – always fall back to Node 20

    return {
        # Raw info
        "files": files,

        # Build detection
        "has_package_json": has_package_json,
        "has_build_dir": has_build_dir,
        "has_dist_dir": has_dist_dir,

        # Project type
        "is_static_site": is_static_site,
        "has_docker": has_docker,

        # Runtime requirements
        "node_version": node_version_required,

        # Deployment target (fixed for this agent)
        "deploy_target": "azure_vm_nginx"
    }
