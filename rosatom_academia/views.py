from django.shortcuts import render, redirect
from .models import Review
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

def rating(request):
    return render(request, 'participant.html')

def user_table(request):
    users = User.objects.all()
    return render(request, 'user_table.html', {'users': users})

def home(request):
    return render(request, 'home.html')

class SignUpGeneral(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class SignUpHR(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup_hr.html'

class SignUpPM(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup_pm.html'

class SignUpParticipant(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup_participant.html'
