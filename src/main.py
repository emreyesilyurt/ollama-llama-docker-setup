from src.llama_utils import ask_llama

def main():
    llama_model = "ollama run llama3:latest"  # Replace with your specific Llama model
    prompt = "Please provide an example prompt for the Llama model."

    response = ask_llama(prompt, llama_model)
    print("Llama Model Response:")
    print(response)

if __name__ == "__main__":
    main()
