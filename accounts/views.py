from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationFrom

class SignUpView(CreateView):
    form_class = CustomUserCreationFrom
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')