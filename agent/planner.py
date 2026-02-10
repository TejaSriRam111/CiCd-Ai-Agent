def plan_pipeline(repo_context, llm, mode):
    prompt = f"""
name: Azure VM Nginx Deployment

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
            npm run build
          fi

      - name: Upload files to Azure VM
        uses: appleboy/scp-action@v0.1.7
        with:
          host: ${{{{ secrets.AZURE_HOST }}}}
          username: ${{{{ secrets.AZURE_USER }}}}
          key: ${{{{ secrets.AZURE_SSH_KEY }}}}
          source: |
            build/*
            dist/*
            *.html
          target: /var/www/html
          strip_components: 1

      - name: Restart nginx
        uses: appleboy/ssh-action@v1.0.0
        with:
          host: ${{{{ secrets.AZURE_HOST }}}}
          username: ${{{{ secrets.AZURE_USER }}}}
          key: ${{{{ secrets.AZURE_SSH_KEY }}}}
          script: sudo systemctl restart nginx
"""
    return prompt
