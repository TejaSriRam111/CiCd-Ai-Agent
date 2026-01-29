from analyzer.tech_detector import detect_tech

def analyze_repo(repo_path):
    tech = detect_tech(repo_path)
    return tech
