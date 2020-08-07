from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('card/index/', views.card_index, name='card_index'),
    path('review/<urlid>/', views.review, name='review'),
    path('getrandomcard/', views.randomizeCard, name='randomize'),
]