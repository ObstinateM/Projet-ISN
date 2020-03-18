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