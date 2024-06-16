from rest_framework import generics, viewsets, filters
from .models import Chat
from serializers import ChatSerializer



class ChatListView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializers_class = ChatSerializer
