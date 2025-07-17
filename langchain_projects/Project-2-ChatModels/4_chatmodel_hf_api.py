import os
from huggingface_hub import InferenceClient
from getpass import getpass
# from dotenv import load_dotenv

# load_dotenv()

# Ensure your token is set
# if "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
#     os.environ["HUGGINGFACEHUB_API_TOKEN"] = getpass("Enter your Hugging Face API token: ")

# Initialize the client directly
client = InferenceClient()

# Make a direct call
try:
    response = client.chat_completion(
        messages=[{"role": "user", "content": "What is the capital of India?"}],
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", #"mistralai/Mistral-7B-Instruct-v0.2",
        max_tokens=50,
    )
    print("Direct API call successful!")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred during the direct API call: {e}")

