def plan_pipeline(repo_context, llm, mode):
    prompt = f"""
You are an AI that generates GitHub Actions workflow files.

ABSOLUTE RULES (NON-NEGOTIABLE):
- Output ONLY valid YAML
- Do NOT include explanations
- Do NOT include markdown
- Do NOT include ``` or ```yaml
- The FIRST line MUST start with: name:
- The output must be directly usable as .github/workflows/ci-cd.yml

TRIGGER:
on:
  push:
    branches:
      - main

GLOBAL REQUIREMENTS:
- Use ubuntu-latest runners
- Always install Node.js 20 using actions/setup-node@v4 BEFORE any npm command
- Never hardcode IPs, usernames, or SSH keys
- Use GitHub Secrets: AZURE_HOST, AZURE_USER, AZURE_SSH_KEY

BUILD RULES:
- If package.json exists:
    - run npm install
    - run npm run build (ignore failure if script does not exist)
- Do NOT use npm run deploy

DEPLOYMENT RULES:
- Target: Azure Ubuntu VM
- Web server: Nginx
- Use SSH and SCP only
- Copy files to /var/www/html
- If build/ exists → deploy build/*
- Else if dist/ exists → deploy dist/*
- Else → deploy repository root
- Restart nginx after deployment

REPOSITORY ANALYSIS (for context only):
{repo_context}

Generate a COMPLETE CI/CD workflow with:
- build job
- deploy job
- proper job dependencies
- valid GitHub Actions syntax

Return ONLY the YAML. NOTHING ELSE.
"""
    return llm(prompt)
