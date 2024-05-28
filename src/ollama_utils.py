import subprocess

def is_service_enabled(service_name):
    try:
        result = subprocess.run(['systemctl', 'is-enabled', service_name], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip() == 'enabled'
        else:
            print(f"Error checking service status: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"Exception occurred: {e}")
        return False

def start_ollama_service():
    if not is_service_enabled("ollama"):
        print("Starting the 'ollama' service...")
        start_result = subprocess.run(["ollama", "start"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if start_result.returncode != 0:
            print(f"Failed to start the 'ollama' service: {start_result.stderr.strip()}")
            return False
    return True
