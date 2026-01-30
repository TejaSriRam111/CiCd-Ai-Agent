def plan_pipeline(repo_context, llm, mode):
    prompt = f"""
You are an autonomous DevOps AI agent.

Repository analysis:
{repo_context}

Your job:
1. Generate CI pipeline
2. Generate CD pipeline
3. Deploy automatically
4. Return a public URL

Rules:
- Use GitHub Actions
- Deploy only on main branch
- Use real platforms (Vercel, Render, EC2)
- Add URL as comment: # DEPLOYMENT_URL

Return ONLY valid YAML.
"""
    return llm(prompt)
