from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import Chat
from .serializers import ChatSerializer


class ChatListView(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['statement']
    ordering_fields = ['date_created']
    ordering = ['-date_created']
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        statement = self.request.query_params.get('statement')
        if statement:
            return Chat.objects.filter(user=user)
        else:
            response_data = {
                'messsage': 'Необходимо выбрать чат!'
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)



