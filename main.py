import requests
import base64
import json

# OpenAI API configuration
OPENAI_API_KEY = ""
HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

# Simulated "encryption" and "decryption" functions
def simple_encrypt(text):
    # Simulating encryption by encoding text to base64
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def simple_decrypt(text):
    # Simulating decryption by decoding text from base64
    return base64.b64decode(text.encode('utf-8')).decode('utf-8')

# Function to send the "encrypted" prompt to OpenAI and receive a response
def send_to_openai(encrypted_prompt):
    url = "https://api.openai.com/v1/chat/completions"

    # Decoding the prompt for demonstration purposes before sending
    decrypted_prompt = simple_decrypt(encrypted_prompt)
    
    # The data payload for the API request
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": decrypted_prompt}
        ]
    }
    
    # Making the API request
    response = requests.post(url, headers=HEADERS, data=json.dumps(data))
    if response.status_code == 200:
        # Extracting the response content
        response_data = response.json()
        if 'choices' in response_data and response_data['choices']:
            # Assuming only one choice is returned and extracting the content
            message_content = response_data['choices'][0]['message']['content']
            return message_content
        else:
            return "No response generated."
    else:
        print("Failed to get response from OpenAI:", response.text)
        return None

# Main workflow function
def full_workflow(user_prompt):
    # Simulating encryption of the user prompt
    encrypted_prompt = simple_encrypt(user_prompt)
    print(f"Encrypted Prompt: {encrypted_prompt}")
    
    # Sending the "encrypted" prompt to OpenAI and getting the response
    response = send_to_openai(encrypted_prompt)
    print("OpenAI Response:", response)

# Example usage
user_prompt = "List 5 ways to build out a resilient supply chain."
full_workflow(user_prompt)
