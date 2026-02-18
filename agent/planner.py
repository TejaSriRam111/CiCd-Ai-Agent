import json
import re


def extract_json(text: str):
    """
    Extract first JSON object from LLM response safely.
    """
    json_match = re.search(r"\{.*\}", text, re.DOTALL)
    if not json_match:
        return None

    try:
        return json.loads(json_match.group())
    except json.JSONDecodeError:
        return None


def plan_pipeline(repo_context, llm, mode="full-devops"):
    prompt = f"""
You are a DevOps expert.

Analyze the repository context and return ONLY valid JSON.

Required format:

{{
  "language": "string",
  "build_command": "string",
  "deploy_dir": "string"
}}

Do not return code.
Do not explain.
Return ONLY JSON.
"""

    response = llm(prompt)

    workflow_plan = extract_json(response)

    if not workflow_plan:
        print("⚠ LLM returned non-JSON response.")
        print("Raw LLM Output:")
        print(response)

        # Fallback safe default
        workflow_plan = {
            "language": "unknown",
            "build_command": "echo Build step",
            "deploy_dir": "build"
        }

        print("⚠ Using fallback workflow plan.")

    return workflow_plan
