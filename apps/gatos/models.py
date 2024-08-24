from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField(max_length=2)
