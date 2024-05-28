import subprocess
from src.ollama_utils import start_ollama_service

def ask_llama(prompt, llama_model):
    if not start_ollama_service():
        return ""
    
    command = ["ollama", "run", llama_model]
    result = subprocess.run(command, input=prompt, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        return result.stdout
    else:
        print(f"Error: {result.stderr}")
        return ""
