from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm()
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {"form":form})

def login(request):
    pass