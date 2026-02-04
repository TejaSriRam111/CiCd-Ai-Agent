import subprocess

def ask_ollama(prompt: str) -> str:
    """
    Sends prompt to local Ollama model and returns response
    """
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout.strip()
