import sys

def main():
    if len(sys.argv) >= 2:
        repo_path = sys.argv[1]
    else:
        repo_path = input("Enter GitHub repo URL or local repo path: ").strip()

    print(f"Running CI/CD AI Agent on: {repo_path}")

if __name__ == "__main__":
    main()
