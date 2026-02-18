import subprocess

def ask_ollama(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "phi"],
        input=prompt.encode("utf-8"),   # force UTF-8 input
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="ignore"))

    # decode safely
    return result.stdout.decode("utf-8", errors="ignore").strip()
