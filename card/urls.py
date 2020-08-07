from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('card/index/', views.card_index, name='card_index'),
    path('review/<urlid>/', views.review, name='review'),
    path('review/', views.review, name='review_alone'),
    path('getrandomcard/', views.randomizeCard, name='randomize'),
    path('option/', views.option, name='option'),
    path('update/<pk>/', views.update, name='update'),
    path('delete/<pk>/', views.delete, name='delete'),
]