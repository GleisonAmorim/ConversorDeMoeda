from django.db import models

class Moeda(models.Model):
    # Nome da moeda, por exemplo, USD, BRL, EUR
    nome = models.CharField(max_length=3, unique=True)
    # Taxa de câmbio da moeda em relação a uma moeda de referência
    cotacao = models.DecimalField(max_digits=10, decimal_places=6)
