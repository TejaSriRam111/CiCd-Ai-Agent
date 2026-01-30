import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)

def ask_claude(prompt: str) -> str:
    response = client.messages.create(
        model="claude-3.5-sonnet-2024-10-22",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
