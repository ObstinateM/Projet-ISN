from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from card.models import Cartes, Review

from random import choice
import datetime
import time

# Create your views here.

@login_required(login_url="../login/")
def create(request):
    if request.method == 'POST':
        form = forms.CreateCard(request.POST, label_suffix='')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id_shared = request.user
            instance.save()
            return redirect('create')
    else:
        form = forms.CreateCard(label_suffix='')
    return render(request, 'card/create.html', {'form':form})

@login_required(login_url="../../login/")
def card_index(request):
    return render(request, 'card/index.html', {})

@login_required(login_url="../login/")
def review(request, urlid=None):
    """ To do :
    Voir comment contourner le fait que la page se refresh pour envoyer l'info du submit
    Il faut que la page, lorsqu'elle se refresh ne change pas
    Donc changement d'url
    donc voir comment ajouter un str dans l'url
    """
    if urlid == None:
        return redirect('randomize')
    else:
        card = Cartes.objects.get(pk=urlid)
        obj, created = Review.objects.get_or_create(
            card_id_id=card.id,
            user_id_id=request.user.id,
        )

        if request.method=='POST' and 'btnform1' in request.POST:
            print(card.id)
            obj.review_level = 1
            obj.review_date = datetime.date.today()
            obj.save()
            return redirect('randomize')

        if request.method=='POST' and 'btnform2' in request.POST:
            print(card.id)
            obj.review_date = datetime.date.today()
            if obj.review_level != 5:
                obj.review_level = obj.review_level + 1
            obj.save()
            return redirect('randomize')

        context = {'card':card}
        return render(request, 'card/review.html', context)

@login_required(login_url="../login/")
def randomizeCard(request):
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
        print(card.id, "///", obj.id)
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
            return redirect('review', urlid=random_pk)
        elif obj.review_level == 2 and datetime.date.today() >= date_3_days:
            loop = False
            return redirect('review', urlid=random_pk)
        elif obj.review_level == 3 and datetime.date.today() >= date_7_days:
            loop = False
            return redirect('review', urlid=random_pk)
        elif obj.review_level == 4 and datetime.date.today() >= date_21_days:
            loop = False
            return redirect('review', urlid=random_pk)
        elif obj.review_level == 5 and datetime.date.today() >= date_42_days:
            loop = False
            return redirect('review', urlid=random_pk)
        else:
            # print("SKIPPED")
            loop = True

def option(request):
    obj = Cartes.objects.all().filter(user_id_shared_id__exact=request.user.id)
    context = {'obj':obj}
    return render(request, 'card/option.html', context)

def update(request, pk):
    card = Cartes.objects.get(id=pk)
    form = forms.CreateCard(instance=card)

    if request.method == 'POST':
        form = forms.CreateCard(request.POST, instance=card)
        print("C VALIDE OU PAS WSHHH", form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('option')

    context = {'form': form}
    return render(request, 'card/update.html', context)

def delete(request, pk):
    card = Cartes.objects.get(id=pk)
    if request.method == 'POST':
        card.delete()
        return redirect('option')
    context = {'card':card}
    return render(request, 'card/delete.html', context)