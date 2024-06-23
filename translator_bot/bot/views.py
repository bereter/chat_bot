from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import Chat
from .serializers import ChatSerializer


class ChatListView(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['date_created']
    ordering = ['-date_created']
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        statement = self.kwargs.get('statement').upper()
        return Chat.objects.filter(user=user, statement=statement)



