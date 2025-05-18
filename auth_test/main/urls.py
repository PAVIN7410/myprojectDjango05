# main/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, ProfileView
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'), # или отдельная главная
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='index'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]