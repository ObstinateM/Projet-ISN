from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

@login_required(login_url="../login/")
def create(request):
    if request.method == 'POST':
        form = forms.CreateCard(request.POST, label_suffix='')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id_shared = request.user
            instance.save()
    else:
        form = forms.CreateCard(label_suffix='')
    return render(request, 'card/create.html', {'form':form})