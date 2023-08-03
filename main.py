import os
from litellm import completion

# Set ENV variables (replace with your actual API keys)
os.environ["OPENAI_API_KEY"] = "your_openai_key"
os.environ["COHERE_API_KEY"] = "your_cohere_key"

def main():
    # Define the messages for the conversation
    messages = [
        {"content": "Hello, how are you?", "role": "user"}
    ]
    
    # OpenAI call using gpt-3.5-turbo model
    openai_response = completion(model="gpt-3.5-turbo", messages=messages)
    print("OpenAI Response:")
    print(openai_response['choices'][0]['message']['content'])
    
    # Cohere call using "command-nightly" model
    cohere_response = completion("command-nightly", messages)
    print("Cohere Response:")
    print(cohere_response['choices'][0]['message']['content'])
    
    # Azure OpenAI call using "chatgpt-test" model
    azure_response = completion("chatgpt-test", messages, azure=True)
    print("Azure OpenAI Response:")
    print(azure_response['choices'][0]['message']['content'])
    
    # OpenRouter call using "google/palm-2-codechat-bison" model
    openrouter_response = completion("google/palm-2-codechat-bison", messages)
    print("OpenRouter Response:")
    print(openrouter_response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
