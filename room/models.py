from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=256)
    owner_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    room_desc = models.TextField(blank=True)

    def __str__(self):
        return self.room_name
