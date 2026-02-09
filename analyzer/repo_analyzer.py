import os
import json


def analyze_repo(repo_path):
    files = os.listdir(repo_path)

    package_json = os.path.join(repo_path, "package.json")
    has_package_json = os.path.exists(package_json)

    has_build_dir = os.path.isdir(os.path.join(repo_path, "build"))
    has_dist_dir = os.path.isdir(os.path.join(repo_path, "dist"))

    is_static_site = any(f.endswith(".html") for f in files)

    node_version = "20"
    if has_package_json:
        try:
            with open(package_json, "r", encoding="utf-8") as f:
                pkg = json.load(f)
                if "engines" in pkg and "node" in pkg["engines"]:
                    node_version = pkg["engines"]["node"]
        except Exception:
            pass

    return {
        "files": files,
        "has_package_json": has_package_json,
        "has_build_dir": has_build_dir,
        "has_dist_dir": has_dist_dir,
        "is_static_site": is_static_site,
        "node_version": node_version,
        "deploy_target": "azure_vm_nginx"
    }
