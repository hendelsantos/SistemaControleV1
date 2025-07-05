from django.db import models

class GiPendenteSemana(models.Model):
    semana = models.CharField(max_length=20)
    gi_realizado = models.DecimalField(max_digits=10, decimal_places=2)
    gi_devido = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Semana {self.semana}"