import requests
import json
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

def openai_process_message(user_message):
    # Set the prompt for OpenAI Api
    prompt = "\"Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations. " + user_message + "\""

    # Call the OpenAI Api to process our prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use a different engine based on your needs
        prompt=prompt,
        max_tokens=100  # Adjust max_tokens as needed
    )
    # Parse the response to get the response text for our prompt
    generated_text = response['choices'][0]['text']
    return generated_text

