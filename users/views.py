from django.shortcuts import redirect, render
from .forms import CustomUserForm
from django.views import View
from django.contrib.auth import login


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list-rooms')

        form = CustomUserForm()
        return render(request, 'registration/register.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list-rooms')

        form = CustomUserForm(request.POST or None)
        if form.is_valid():
            # Model Form Returns the object created
            user = form.save()
            login(request, user)
            return redirect('list-rooms')

        return render(request, 'registration/register.html', {
            'form': form
        })
