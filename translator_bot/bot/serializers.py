from rest_framework import serializers
from .models import Chat
from django.contrib.auth.models import User
import openai
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv('AI_KEY')

def ask_ai(message):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        message=[{'role': 'user', 'content': message}]
    )
    answer = response.choices[0].message.content.strip()
    return answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Chat
        fields = ['user', 'message_user', 'message_ai', 'date_created', 'statement']
        read_only_fields = ['message_ai']

    def create(self, validated_data):
        response_ai = ask_ai(validated_data['message_user'])
        validated_data['message_ai'] = response_ai
        return Chat.objects.create(**validated_data)
