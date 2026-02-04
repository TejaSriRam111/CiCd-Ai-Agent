def plan_pipeline(repo_context, llm, mode):
    prompt = f"""
You generate GitHub Actions workflow files.

STRICT RULES (MANDATORY):
- Output ONLY valid YAML
- Do NOT include explanations
- Do NOT include markdown
- Do NOT include ```yaml or ```
- The FIRST line MUST start with: name:
- The output must be directly usable as .github/workflows/ci-cd.yml

Repository analysis:
{repo_context}

Generate a CI/CD pipeline with these requirements:
- Trigger on push to main branch
- Include build stage
- Include deployment stage
- Use GitHub Actions syntax
- If deploying, add deployment URL as a YAML comment:
  # DEPLOYMENT_URL: https://example.com

ONLY return the YAML. NOTHING else.
"""
    return llm(prompt)
