from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {"form":form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
    else:
        form = AuthenticationForm() 
    return render(request, 'accounts/login.html', {'form':form})

