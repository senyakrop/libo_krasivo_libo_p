from django.shortcuts import render, redirect
from .models import Review
from .models import User

def home_page(request):
    return render(request, 'home.html')

def user_table(request):
    users = User.objects.all()
    return render(request, 'user_table.html', {'users': users})