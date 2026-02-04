def plan_pipeline(repo_context, llm, mode):
    prompt = f"""
You generate GitHub Actions workflow YAML files.

STRICT RULES (MANDATORY – DO NOT VIOLATE):
- Output ONLY valid YAML
- Do NOT include explanations, comments outside YAML, or markdown
- Do NOT include ```yaml or ```
- The FIRST line MUST be exactly: name:
- The workflow MUST be valid for GitHub Actions
- Use ONLY the trigger format shown below (do not change it)

MANDATORY TRIGGER FORMAT (EXACT):
on:
  push:
    branches:
      - main

DO NOT use:
- on: [push]
- on: push
- branches outside push

Repository analysis:
{repo_context}

Generate a CI/CD pipeline with:
- A build job
- A deploy job
- GitHub Actions syntax only
- Ubuntu runner
- If deployment is included, add a YAML comment at the end:
  # DEPLOYMENT_URL: https://example.com

Return ONLY the YAML. NOTHING else.
"""
    return llm(prompt)
