from django.db import models

class PM05Item(models.Model):
    catalog_envio = models.CharField("Catalog de Envio", max_length=50)
    catalog_ersa = models.CharField("Catalog ERSA", max_length=50, blank=True, null=True)
    descricao = models.CharField("Descrição", max_length=255)
    numero_serie = models.CharField("Número de Série", max_length=100, blank=True, null=True)
    quantidade = models.PositiveIntegerField("Quantidade", default=1)
    fornecedor_enviado = models.CharField("Fornecedor Enviado", max_length=100, blank=True, null=True)
    codigo_supplier = models.CharField("Código Supplier", max_length=50, blank=True, null=True)
    data_envio = models.DateField("Data de Envio para Fornecedor")
    numero_invoice = models.CharField("Número da Invoice", max_length=100, blank=True, null=True)
    numero_pm05 = models.CharField("Número PM05", max_length=100, blank=True, null=True)
    nf_saida = models.CharField("Nota Fiscal de Saída", max_length=100, blank=True, null=True)
    nf_retorno = models.CharField("Nota de Retorno", max_length=100, blank=True, null=True)
    obs1 = models.CharField("Obs 1", max_length=255, blank=True, null=True)
    obs2 = models.CharField("Obs 2", max_length=255, blank=True, null=True)
    obs3 = models.CharField("Obs 3", max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.catalog_envio} - {self.descricao}"

class PM05Foto(models.Model):
    item = models.ForeignKey(PM05Item, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='pm05_fotos/')
    descricao = models.CharField(max_length=255, blank=True, null=True)

class PM05Arquivo(models.Model):
    item = models.ForeignKey(PM05Item, on_delete=models.CASCADE, related_name='arquivos')
    arquivo = models.FileField(upload_to='pm05_arquivos/')
    descricao = models.CharField(max_length=255, blank=True, null=True)
