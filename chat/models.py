from django.db import models
from django.contrib.auth import get_user_model
from room.models import Room

User = get_user_model()


class Message(models.Model):
    author = models.ForeignKey(
        User, related_name='author_messages', on_delete=models.CASCADE)
    room_associated = models.ForeignKey(
        Room, related_name='room_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_15_messages(self):
        return Message.objects.order_by('timestamp').all()[:15]
