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

@login_required(login_url="../login/")
def card_index(request):
    return render(request, 'card/index.html', {})

@login_required(login_url="../login/")
def review(request):
    title = "Titre Test"
    content = "Contenu Test bla lorem ipsum"
    if request.method == 'POST':
        form = forms.ReviewCard(request.POST)
        if form.is_valid():
            pass # Do some stuff  
    else:
        form = forms.ReviewCard()
    return render(request, 'card/review.html', {'title':title, 'content':content, 'form':form})