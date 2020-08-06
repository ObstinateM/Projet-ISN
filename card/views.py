from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from card.models import Cartes, Review

from random import choice
import datetime

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

    loop = True
    i = 0
    while loop and i < len(Cartes.objects.filter(user_id_shared_id__exact=request.user.id).values_list('pk', flat=True))*4:
        i = i + 1
        pks = Cartes.objects.filter(user_id_shared_id__exact=request.user.id).values_list('pk', flat=True)
        if len(pks) == 0:
            loop = False
            return redirect('/create/')
        random_pk = choice(pks)
        card = Cartes.objects.get(pk=random_pk)
        obj, created = Review.objects.get_or_create(
            card_id_id=card.id,
            user_id_id=request.user.id,
        )
        date_3_days = obj.review_date + datetime.timedelta(days=3)
        date_7_days = obj.review_date + datetime.timedelta(days=7)
        date_21_days = obj.review_date + datetime.timedelta(days=21)
        date_42_days = obj.review_date + datetime.timedelta(days=42)
        # print(card.id)
        # print(date_3_days, date_7_days, date_21_days, date_42_days)
        # print(obj.review_level == 1)
        # print(obj.review_level == 2 and datetime.date.today() >= date_3_days)
        # print(obj.review_level == 3 and datetime.date.today() >= date_7_days)
        # print(obj.review_level == 4 and datetime.date.today() >= date_21_days)
        # print(obj.review_level == 5 and datetime.date.today() >= date_42_days)
        if obj.review_level == 1:
            loop = False
        elif obj.review_level == 2 and datetime.date.today() >= date_3_days:
            loop = False
        elif obj.review_level == 3 and datetime.date.today() >= date_7_days:
            loop = False
        elif obj.review_level == 4 and datetime.date.today() >= date_21_days:
            loop = False
        elif obj.review_level == 5 and datetime.date.today() >= date_42_days:
            loop = False
        else:
            print("SKIPPED")
            loop = True

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

