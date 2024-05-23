import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def lambda_handler(event, context):
    body = json.loads(event['body'])
    user_message = body.get('message', '')

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=user_message,
        max_tokens=150
    )

    chatbot_reply = response.choices[0].text.strip()

    return {
        'statusCode': 200,
        'body': json.dumps({'reply': chatbot_reply})
    }
