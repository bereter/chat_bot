from rest_framework import serializers
from .models import Chat
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Chat
        fields = ['user', 'message_user', 'message_ai', 'created', 'statement']
