import os


def write_workflow(repo_path, plan):
    workflow_dir = os.path.join(repo_path, ".github", "workflows")
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_file = os.path.join(workflow_dir, "ci-cd.yml")

    deploy_logic = ""
    if plan["deploy_dir"] == "build":
        deploy_logic = "scp -r build/*"
    elif plan["deploy_dir"] == "dist":
        deploy_logic = "scp -r dist/*"
    else:
        deploy_logic = "scp -r ./*"

    workflow_yaml = f"""name: Azure VM Nginx Deployment

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Build project (if applicable)
        run: |
          if [ -f package.json ]; then
            npm install
            npm run build || echo "No build script"
          fi

      - name: Setup SSH
        run: |
          mkdir -p ~/.ssh
          echo "${{{{ secrets.AZURE_SSH_KEY }}}}" > ~/.ssh/id_ed25519
          chmod 600 ~/.ssh/id_ed25519
          ssh-keyscan -H ${{{{ secrets.AZURE_HOST }}}} >> ~/.ssh/known_hosts

      - name: Deploy to Azure VM
        run: |
          {deploy_logic} ${{{{ secrets.AZURE_USER }}}}@${{{{ secrets.AZURE_HOST }}}}:/var/www/html/

      - name: Restart nginx
        run: |
          ssh ${{{{ secrets.AZURE_USER }}}}@${{{{ secrets.AZURE_HOST }}}} "sudo systemctl restart nginx"
"""

    with open(workflow_file, "w", encoding="utf-8", newline="\n") as f:
        f.write(workflow_yaml)
