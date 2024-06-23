from rest_framework import serializers
from .models import Chat
import openai
from g4f.client import Client


# from dotenv import load_dotenv, find_dotenv
# import os
# load_dotenv(find_dotenv())
# openai.api_key = os.getenv('AI_KEY')

client = Client()

def ask_ai(message):
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[{
            'role': 'user',
            'content': message
        }]
    )
    # print(response.choices[0].message.content)
    answer = response.choices[0].message.content.strip()
    return answer


class ChatSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Chat
        fields = ['user', 'message_user', 'message_ai', 'date_created', 'statement']
        read_only_fields = ['message_ai']

    def create(self, validated_data):
        response_ai = ask_ai(validated_data['message_user'])
        validated_data['message_ai'] = response_ai
        return Chat.objects.create(**validated_data)
