from django.shortcuts import render
from .forms import CustomUserForm
from django.views import View


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserForm()
        return render(request, 'registration/register.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        pass
