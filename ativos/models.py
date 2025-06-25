from django.db import models

class Ativo(models.Model):
    numero_ativo = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=255)
    catalog = models.CharField(max_length=50)
    local_armazenamento = models.CharField(max_length=100)
    data_inventario = models.DateField()
    obs1 = models.CharField(max_length=255, blank=True, null=True)
    obs2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.numero_ativo} - {self.descricao}"

class FotoAtivo(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='ativos_fotos/')
    descricao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Foto de {self.ativo.numero_ativo}"
