# main/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class RegisterView(TemplateView):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # После регистрации перенаправляем на страницу входа
            return redirect('login')
        return self.render_to_response({'form': form})

class ProfileView(TemplateView):
    template_name = 'profile.html'

class IndexView(TemplateView):
    template_name = 'index.html'