from django.db import models

class GiPendente(models.Model):
    catalogo = models.CharField(max_length=50)
    bin = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    onde_foi_usado = models.CharField(max_length=255)
    ordem = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    unit = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return f"{self.catalogo} - {self.descricao}"
