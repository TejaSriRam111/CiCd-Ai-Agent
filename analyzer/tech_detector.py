import os

def detect_tech(repo_path):
    files = os.listdir(repo_path)

    if "pom.xml" in files:
        return {
            "language": "java",
            "build_tool": "maven",
            "ci": "github-actions"
        }

    if "build.gradle" in files:
        return {
            "language": "java",
            "build_tool": "gradle",
            "ci": "github-actions"
        }

    if "package.json" in files:
        return {
            "language": "node",
            "build_tool": "npm",
            "ci": "github-actions"
        }

    if "requirements.txt" in files:
        return {
            "language": "python",
            "build_tool": "pip",
            "ci": "github-actions"
        }

    return {
        "language": "unknown",
        "build_tool": "unknown",
        "ci": "github-actions"
    }
