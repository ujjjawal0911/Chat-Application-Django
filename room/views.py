from django.shortcuts import render
from django.views import View
from .models import Room
from .forms import RoomForm


class CreateRoom(View):
    def post(self, request, *args, **kwargs):
        pass

# Get Room Info


class RoomInfo(View):
    pass


class UpdateRoomInfo(View):
    pass


class DeleteRoom(View):
    pass


class ListRoom(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'room/list-rooms.html', {
            'form': RoomForm()
        })
