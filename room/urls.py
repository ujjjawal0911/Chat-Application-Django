from django.urls import path
from .views import (
    CreateRoom,
    DeleteRoom,
    UpdateRoom,
    ListRoom
)

urlpatterns = [
    # Create Room
    path('create/', CreateRoom.as_view(), name='create-room'),
    # Update Room Data
    path('update/<str:room_name>/', UpdateRoom.as_view(), name='update-room'),
    # Delete Room
    path('delete/<str:room_name>/', DeleteRoom.as_view(), name='delete-room'),
    # List Rooms
    path('', ListRoom.as_view(), name='list-rooms'),
]
