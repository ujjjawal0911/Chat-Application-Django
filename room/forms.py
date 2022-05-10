from django import forms
from django.forms import ModelForm
from room.models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'room_desc']

        labels = {
            'room_name': ('Enter Room Name'),
            'room_desc': ('Enter Room Description')
        }

        widgets = {
            'room_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Room Name',
                }
            ),
            'room_desc': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Room Information',
                    'rows': '5',
                    'style': 'height:100%;',
                }
            )
        }
