from django.db import models
from uuid import uuid4

# Create your models here.
class Usuario(models.Model):
    id_user = models.UUIDField(primary_key=True,default=uuid4)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome