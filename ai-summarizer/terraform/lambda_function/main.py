import os
import json
import openai

# Get API Key from environment variable OPENAI_API_KEY
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def lambda_handler(event, context):
    # Parse the incoming JSON payload
    body = json.loads(event['body'])
    user_message = body.get('message', '')

    # Create a chat completion using OpenAI's GPT-3.5-turbo
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    # Structure the return response for API Gateway
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': response.choices[0].message.content
    }
