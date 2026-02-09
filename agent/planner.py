def plan_pipeline(repo_context, llm, mode):
    prompt = f"""
You generate GitHub Actions workflow YAML.

STRICT RULES:
- Output ONLY valid YAML
- No markdown, no explanations
- First line MUST be: name:
- GitHub Actions syntax only

MANDATORY TRIGGER:
on:
  push:
    branches:
      - main

DEPLOYMENT TARGET:
- Azure Ubuntu VM
- Nginx web server
- Use SSH + SCP
- Copy files to /var/www/html
- Restart nginx
- NEVER use npm run deploy

BUILD LOGIC:
- If package.json exists → npm install && npm run build
- If build/ exists → deploy build/*
- If dist/ exists → deploy dist/*
- Else → deploy repository root

Repository analysis:
{repo_context}

Generate CI/CD pipeline now.
"""
    return llm(prompt)
