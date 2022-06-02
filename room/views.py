from django.shortcuts import redirect, render
from django.views import View
from .models import Room
from .forms import RoomForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateRoom(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = RoomForm()
        return render(request, 'room/create-room.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = RoomForm(request.POST)

        if form.is_valid():
            # Getting the Instance of the User Who Created the Room
            instance = form.save(commit=False)
            instance.owner_id = request.user
            instance.save()
            return redirect('list-rooms')

        return render(request, 'room/create-room.html', {
            'form': form,
        })


class UpdateRoom(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        room = Room.objects.get(room_name=kwargs['room_name'])
        form = RoomForm(instance=room)
        return render(request, 'room/create-room.html', {
            'room': room,
            'form': form,
            'update': True
            # Using same Template for Create and Update so
            # To Identify wether request for Update or Create
            # So to change Hrefs and Few Names
        })

    def post(self, request, *args, **kwargs):
        room = Room.objects.get(room_name=kwargs['room_name'])
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect('list-rooms')

        return render(request, 'room/create-room.html', {
            'room': room,
            'form': form,
            'update': True
        })


class DeleteRoom(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        room_name = kwargs['room_name']
        room = Room.objects.get(room_name=room_name)
        room.delete()
        return redirect('list-rooms')


class ListRoom(View):
    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        return render(request, 'room/list-rooms.html', {
            'rooms': rooms
        })
