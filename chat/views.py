from django.shortcuts import redirect, render
import random
import math
from room.models import Room
from django.contrib import messages

# Function to generate 6 digit code


def generate_code():
    # storing strings in a list
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(6):
        index = math.floor(random.random()*10)
        random_str += str(digits[index])

    return random_str


def chatroom(request, room_name):
    try:
        Room.objects.get(room_name=room_name)
    except:
        messages.warning(request, 'No such Room Exists.')
        return redirect('list-rooms')
    else:
        if not request.user.is_authenticated:
            if 'temp_id' not in request.session:
                request.session['temp_id'] = generate_code()
                username = 'AnonymousUser-'+request.session['temp_id']
                request.session['username'] = username
                request.session.modified = True
        return render(request, 'chat/chatroom.html', {
            'room_name': room_name,
        })
