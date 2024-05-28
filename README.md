
# Ollama and Llama Model Utilities

This repository contains utility scripts to help you start the Ollama server and interact with Llama models.

## Files

- `src/ollama_utils.py`: Contains utility functions for starting the Ollama service and checking if it's enabled.
- `src/llama_utils.py`: Contains functions for interacting with the Llama models.
- `src/main.py`: Demonstrates how to use these utilities.
- `Dockerfile`: Docker configuration for the project.
- `docker-compose.yml`: Docker Compose configuration for the project.
- `requirements.txt`: Python dependencies for the project.

## Usage

### Docker Setup

1. **Build and run the Docker container**:
   ```bash
   docker-compose up --build
   ```

2. **Stop the Docker container**:
   ```bash
   docker-compose down
   ```

### Running Locally

1. **Check and start the Ollama service**:
   ```python
   from src.ollama_utils import start_ollama_service
   
   if start_ollama_service():
       print("Ollama service is running.")
   else:
       print("Failed to start Ollama service.")
   ```

2. **Use Llama models**:
   ```python
   from src.llama_utils import ask_llama
   
   llama_model = "llama2"  # Replace with your specific Llama model
   prompt = "Please provide an example prompt for the Llama model."
   
   response = ask_llama(prompt, llama_model)
   print("Llama Model Response:")
   print(response)
   ```

3. **Run the example**:
   ```bash
   python src/main.py
   ```

### Requirements

- Python 3.6+
- \`subprocess\` module (built-in)
- Docker and Docker Compose installed
- Ollama and Llama models installed and configured on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ollama-llama-repo.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd ollama-llama-repo
   ```

3. Run the example locally:
   ```bash
   python src/main.py
   ```

4. Build and run with Docker:
   ```bash
   docker-compose up --build
   ```

# ollama-llama-docker-setup
