def plan_pipeline(repo_context, llm, mode):
    """
    LLM is ONLY used to decide build output directory.
    Workflow structure is fixed and safe.
    """

    if repo_context.get("has_build_dir"):
        deploy_dir = "build"
    elif repo_context.get("has_dist_dir"):
        deploy_dir = "dist"
    else:
        deploy_dir = "root"

    return {
        "deploy_dir": deploy_dir
    }
