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

@login_required(login_url="../../login/")
def card_index(request):
    return render(request, 'card/index.html', {})

@login_required(login_url="../login/")
def review(request):
    """ To do :
    - Ajouter un filtre ( ID de l'user + Review date > from now )
    - récuperer l'id de l'user --> request.user.id
    - Gestion des boutons -> Deux forms

    POUR DEMAIN : GET_OR_CREATE DANS LA TABLE CARD_REVIEW ET CHECK SI REVIEW.DATE >= X DAYS >= FROM NOW

    """
    #pks = Cartes.objects.values_list('pk', flat=True)
    pks = Cartes.objects.filter(user_id_shared_id__exact=request.user.id).values_list('pk', flat=True)
    if len(pks) == 0:
        return redirect('/create/')
    random_pk = choice(pks)
    card = Cartes.objects.get(pk=random_pk)
    if request.method == 'POST':
        form = forms.ReviewCard(request.POST)
        if form.is_valid():
            pass # Do some stuff  
            """
            card.user == request.user
            """
    else:
        form = forms.ReviewCard()
    context = {'card':card, 'form':form}
    return render(request, 'card/review.html', context)

