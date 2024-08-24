from django.db import models

class Piada(models.Model):
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.conteudo[:50]