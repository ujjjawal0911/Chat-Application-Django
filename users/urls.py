from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password-change', auth_views.PasswordChangeView.as_view(),
         name='password-change'),
    path('password-change-done', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
]
