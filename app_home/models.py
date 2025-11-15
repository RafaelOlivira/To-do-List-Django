from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=100,unique=True)
    senha = models.CharField(max_length=128)
    def __str__(self):
        return self.usuario