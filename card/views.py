from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

@login_required(login_url="../login/")
def create(request):
    if request.method == 'POST':
        form = forms.CreateCard(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id_shared = request.user
            instance.save()
    else:
        form = forms.CreateCard()
    return render(request, 'card/create.html', {'form':form})