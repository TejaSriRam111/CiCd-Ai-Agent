import json

def plan_pipeline(repo_context, llm, mode="full-devops"):
    prompt = f"""
You are a DevOps expert.

Analyze the following repository context and return ONLY a valid JSON object.

Repository context:
{repo_context}

Return JSON in this exact format:

{{
  "language": "string",
  "build_command": "string",
  "deploy_dir": "string"
}}

Return ONLY valid JSON. Do not explain anything.
"""

    response = llm(prompt)

    try:
        workflow_plan = json.loads(response)
    except json.JSONDecodeError:
        print("❌ LLM did not return valid JSON.")
        print("LLM Response:")
        print(response)
        raise ValueError("Invalid JSON returned from LLM")

    return workflow_plan
