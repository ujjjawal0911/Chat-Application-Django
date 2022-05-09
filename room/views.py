from django.shortcuts import render
from django.views import View
from .models import Room


class CreateRoom(View):
    pass

# Get Room Info


class RoomInfo(View):
    pass


class UpdateRoomInfo(View):
    pass


class DeleteRoom(View):
    pass


class ListRoom(View):
    model = Room
    template_name = ".html"
    pass
