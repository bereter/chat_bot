from django.db import models
from django.contrib.auth.models import User



class Chat(models.Model):
    """Модель чата"""

    business = 'BU'
    inventions = 'IN'
    fashion = 'FA'

    CATEGORY = [
        (business, 'Бизнес'),
        (inventions, 'Изобретения'),
        (fashion, 'Мода')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_user = models.TextField()
    message_ai = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    statement = models.CharField(max_length=2, choices=CATEGORY)

    def __str__(self):
        return f'{self.user.username} : {self.message_user[0:20]}'
