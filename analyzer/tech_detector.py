import os

def get_all_files(repo_path):
    file_list = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            file_list.append(file)
    return file_list


def detect_tech(repo_path):
    files = get_all_files(repo_path)

    if "pom.xml" in files:
        return {"language": "java", "build_tool": "maven", "ci": "github-actions"}

    if "build.gradle" in files:
        return {"language": "java", "build_tool": "gradle", "ci": "github-actions"}

    if "package.json" in files:
        return {"language": "node", "build_tool": "npm", "ci": "github-actions"}

    if "requirements.txt" in files:
        return {"language": "python", "build_tool": "pip", "ci": "github-actions"}

    if "index.html" in files:
        return {"language": "html", "build_tool": "none", "ci": "github-actions"}

    return {"language": "unknown", "build_tool": "unknown", "ci": "github-actions"}
