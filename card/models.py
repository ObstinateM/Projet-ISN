from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cartes(models.Model):
    id = models.AutoField(primary_key=True)
    user_id_shared = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    card_id = models.ForeignKey(Cartes, on_delete=models.CASCADE, default=None) # Ajouter QUE Cartes.id
    review_date = models.DateField(auto_now=True)
    review_level = models.IntegerField()
