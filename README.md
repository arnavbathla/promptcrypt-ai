# PromptCrypt 

[PromptCrypt](https://arxiv.org/abs/2402.05868) is proposed as an interesting technique to secure LLMs in a recent paper. They mention the use of emojis, which is a great way to encrypt prompts from humans. 

This Python script demonstrates how to integrate with the OpenAI API using a simple "encryption" and "decryption" mechanism for the prompts. It uses Base64 encoding as a simulated form of encryption to showcase how data might be manipulated before being sent to the API. This example specifically uses GPT-3.5, but feel free to switch between models.

<img width="1506" alt="Screenshot 2024-02-11 at 9 00 17 PM" src="https://github.com/arnavbathla/promptcrypt-ai/assets/77173537/01f6d58c-28bd-482b-ac9a-e443a1374e23">


## Requirements

- Python 3.x
- `requests` library

Ensure you have the necessary Python version and the `requests` library installed. You can install `requests` using pip if you haven't already:

```bash

pip install requests

```
## How It Works
Encryption/Decryption: The script simulates encryption and decryption using Base64 encoding and decoding, respectively.

Sending Encrypted Prompts: Encrypted prompts are decrypted back to plain text within the script before being sent to the OpenAI API.

API Request: A POST request is made to the OpenAI API with the decrypted prompt, and the response is processed and printed.

## Usage
To use this script, you simply need to call the full_workflow function with a prompt as the argument
