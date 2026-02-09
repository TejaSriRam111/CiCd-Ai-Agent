def plan_pipeline(repo_context, llm, mode):
    prompt = f"""
You generate GitHub Actions workflow YAML.

ABSOLUTE RULES:
- Output ONLY valid YAML
- NO markdown, NO explanations, NO ``` blocks
- FIRST line MUST be: name:
- GitHub Actions syntax ONLY

FORBIDDEN:
- exists(), fileExists()
- Node.js 14 or lower
- actions/setup-node@v2 or v3
- cp to /var/www/html without SSH
- password-based SSH
- npm run deploy

MANDATORY:
- Use actions/setup-node@v4
- Use Node.js 20
- Use bash for file checks
- Deploy ONLY via SSH + SCP
- Use GitHub secrets:
  AZURE_HOST, AZURE_USER, AZURE_SSH_KEY

BUILD LOGIC (BASH):
- If package.json exists → npm install && npm run build || true

DEPLOY LOGIC (BASH):
- If build/ exists → deploy build/*
- Else if dist/ exists → deploy dist/*
- Else → deploy repo root
- Target: /var/www/html
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
