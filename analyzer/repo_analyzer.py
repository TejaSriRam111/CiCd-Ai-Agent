import os


def analyze_repo(repo_path):
    files = os.listdir(repo_path)

    has_package_json = "package.json" in files
    has_docker = "Dockerfile" in files

    has_build_dir = os.path.isdir(os.path.join(repo_path, "build"))
    has_dist_dir = os.path.isdir(os.path.join(repo_path, "dist"))

    is_static_site = any(
        f.endswith(".html") for f in files
    )

    return {
        "files": files,

        # Build-related
        "has_package_json": has_package_json,
        "has_build_dir": has_build_dir,
        "has_dist_dir": has_dist_dir,

        # Project type
        "is_static_site": is_static_site,
        "has_docker": has_docker,

        # Deployment target (fixed for your agent)
        "deploy_target": "azure_vm_nginx"
    }
