def plan_pipeline(repo_context, llm, mode):
    prompt = f"""
You generate GitHub Actions workflow YAML.

ABSOLUTE RULES:
- Output ONLY valid YAML
- NO explanations
- NO markdown
- NO ``` blocks
- FIRST line MUST be: name:
- GitHub Actions syntax ONLY

FORBIDDEN (NEVER USE):
- working-dir
- working_directory
- continue:
- exists()
- if:
- azure/login
- appleboy
- Node.js 14 or lower
- actions/setup-node@v2 or v3
- npm run deploy

MANDATORY:
- Use actions/checkout@v4
- Use actions/setup-node@v4
- Node.js version MUST be 20
- ALL logic inside bash (run: |)
- Deploy using SSH + SCP ONLY
- Use GitHub Secrets:
  AZURE_HOST
  AZURE_USER
  AZURE_SSH_KEY

BUILD LOGIC (BASH):
- If package.json exists → npm install && npm run build || true

DEPLOY LOGIC (BASH):
- If build/ exists → deploy build/*
- Else if dist/ exists → deploy dist/*
- Else → deploy repository root
- Target directory: /var/www/html
- Restart nginx

TRIGGER:
on:
  push:
    branches:
      - main

REPOSITORY CONTEXT:
{repo_context}

Generate ONE job named build-and-deploy.
Return ONLY YAML.
"""
    return llm(prompt)
