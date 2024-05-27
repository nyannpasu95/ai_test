import openai
import os
import json
from openai import OpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

def lambda_handler(event, context):
    body = json.loads(event['body'])
    user_message = body.get('message', '')
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    chatbot_reply = completion.choices[0].message['content'].strip()

    return {
        'statusCode': 200,
        'body': json.dumps({'reply': chatbot_reply})
    }
