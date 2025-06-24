from django.db import models

class NotaFiscal(models.Model):
    numero = models.CharField("Número da Nota", max_length=30)
    empresa = models.CharField("Empresa", max_length=100, blank=True)
    data_emissao = models.DateField("Data de Emissão", null=True, blank=True)
    valor = models.DecimalField("Valor", max_digits=12, decimal_places=2, null=True, blank=True)
    mes_entrada = models.CharField("Mês de Entrada", max_length=7, blank=True, help_text="Formato: MM/YYYY")
    arquivo = models.FileField("Arquivo PDF", upload_to='notas_fiscais/')
    data_upload = models.DateTimeField("Data de Upload", auto_now_add=True)

    def __str__(self):
        return f"{self.numero} - {self.empresa}"
