from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
import os
import openai
from dotenv import load_dotenv

# load the environment variables
load_dotenv()

# Initialize the Line bot API
line_bot_api = MessagingApi(
    api_client=ApiClient(
        configuration=Configuration(
            channel_secret=os.getenv('LINE_CHANNEL_SECRET')
        )
    )
)

# Set up OpenAI API credentials
openai.api_key = os.getenv('OPENAI_API_KEY')

def generateMessage(prompt):
    # Generate a unique message using OpenAI
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the generated message from the OpenAI response
    generated_message = response.choices[0].text.strip()
    return generated_message

def sendMessages(reply_token: str, messages: list):
    # Send the generated messages to the user
    line_bot_api.reply_message(
        reply_token=reply_token,
        messages=messages
    )

# Define the Lambda handler
def app(event, context):
    # Parse the request body
    body = event['body']
    signature = event['headers']['x-line-signature']

    # Handle the request
    try:
        handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        print(e)

    return {
        'statusCode': 200,
        'body': 'OK'
    }

