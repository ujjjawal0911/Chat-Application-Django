from django.shortcuts import render
import random
import math

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
    if not request.user.is_authenticated:
        request.session['temp_id'] = generate_code()
        username = 'AnonymousUser-'+request.session['temp_id']
        request.session['username'] = username
        request.session.modified = True
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name,
    })
