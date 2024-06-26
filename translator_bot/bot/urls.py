from django.urls import path, include
from .views import ChatListView

urlpatterns = [
    path('chat/<str:statement>/', ChatListView.as_view({'get': 'list', 'post': 'create'})),
    path('chat/<int:pk>/', ChatListView.as_view({'delete': 'destroy'})),
]