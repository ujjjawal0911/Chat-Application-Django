from django.shortcuts import redirect, render
from django.views import View
from .models import Room
from .forms import RoomForm


class CreateRoom(View):
    def get(self, request, *args, **kwargs):
        form = RoomForm()
        return render(request, 'room/create-room.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = RoomForm(request.POST)

        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            instance = form.save(commit=False)
            print(request.user)
            instance.owner_id = request.user
            instance.save()
            return redirect('list-rooms')

        return render(request, 'room/create-room.html', {
            'form': form,
        })

# Get Room Info


class RoomInfo(View):
    pass


class UpdateRoomInfo(View):
    pass


class DeleteRoom(View):
    pass


class ListRoom(View):
    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        return render(request, 'room/list-rooms.html', {
            'rooms': rooms
        })
