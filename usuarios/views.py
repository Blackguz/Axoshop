from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    # form_class = LoginForm


class RegistrarView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('usuarios:login')
    template_name = "auth/user_form.html"

    def form_valid(self, form):
        user = form.save()
        user.save()

        return super().form_valid(form)