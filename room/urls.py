from django.urls import path
from .views import (
    CreateRoom,
    RoomInfo,
    UpdateRoomInfo,
    DeleteRoom,
    ListRoom
)

urlpatterns = [
    # Create Room
    path('create/', CreateRoom.as_view(), name='create-room'),
    # Get Room Info
    path('<str:room_name>/', RoomInfo.as_view(), name='info-room'),
    # Update Room Data
    path('update/<str:room_name>/', UpdateRoomInfo.as_view(), name='update-room'),
    # Delete Room
    path('delete/<str:room_name>/', DeleteRoom.as_view(), name='delete-room'),
    # List Rooms
    path('', ListRoom.as_view(), name='list-rooms'),
]
