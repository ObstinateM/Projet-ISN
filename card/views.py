from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from card.models import Cartes

from random import choice


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
    pks = Cartes.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_obj = Cartes.objects.get(pk=random_pk)
    card = random_obj
    if request.method == 'POST':
        form = forms.ReviewCard(request.POST)
        if form.is_valid():
            pass # Do some stuff  
    else:
        form = forms.ReviewCard()
    return render(request, 'card/review.html', {'card':card, 'form':form})

