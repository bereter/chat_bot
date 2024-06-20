from django.http import QueryDict
from rest_framework import generics, viewsets, filters, status
from rest_framework.response import Response

from .models import Chat
from .serializers import ChatSerializer


class ChatListView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


