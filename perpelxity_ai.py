from openai import OpenAI
import os
import requests

# It's recommended to store your API key as an environment variable
# For demonstration, you can replace os.getenv() with your actual key
# PPLX_API_KEY = "YOUR_PERPLEXITY_API_KEY"
# PPLX_API_KEY = os.getenv("PERPLEXIITY_API_KEY") 
# PPLX_API_KEY = PPLX_API_KEY or "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"
# print("Using Perplexity AI API Key:", PPLX_API_KEY)
# client = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai/chat/completions")

# response = client.chat.completions.create(
#     model="sonar-medium-online",  # Or other available models like "sonar-pro", "llama-3-sonar-large-32k-online"
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "What are the latest advancements in AI?"}
#     ]
# )

# print(response.choices[0].message.content)

# print("Different approach")


# Set up the API endpoint and headers
url = "https://api.perplexity.ai/chat/completions"
PPLX_API_KEY = os.getenv("PERPLEXIITY_API_KEY") 
PPLX_API_KEY = PPLX_API_KEY or "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"
headers = {
    "Authorization": f"Bearer {PPLX_API_KEY}",  # Replace with your actual API key
    "Content-Type": "application/json"
}

# Define the request payload
payload = {
    "model": "sonar-pro",
    "messages": [
        {"role": "user", "content": "What were the results of the 2025 Wimbledon Finals?"}
    ]
}

# Make the API call
response = requests.post(url, headers=headers, json=payload)

# Print the AI's response
#print(response.json()) # replace with 
print(response.json()["choices"][0]['message']['content']) 