from django.db import models

class Demanda(models.Model):
    nome = models.CharField("Nome do solicitante", max_length=255)
    descricao = models.TextField("Descrição detalhada")
    catalogo = models.CharField("Catalog", max_length=17, blank=True, null=True)  # Agora não obrigatório
    quantidade = models.PositiveIntegerField("Quantidade")
    data_criacao = models.DateTimeField("Data de criação", auto_now_add=True)
    cotacao_pdf = models.FileField("Cotação (PDF)", upload_to="cotacoes/", blank=True, null=True)
    

    ETAPAS = [
        ('aberto', 'Aberto'),
        ('cotado', 'Cotado'),
        ('pr', 'PR Criada'),
        ('finalizado', 'Finalizado'),
    ]
    etapa = models.CharField(
        "Etapa",
        max_length=20,
        choices=ETAPAS,
        default='aberto'
    )

    def __str__(self):
        return f'{self.nome} - {self.catalogo} ({self.get_etapa_display()})'


class Pedido(models.Model):
    demanda = models.OneToOneField(
        Demanda,
        on_delete=models.CASCADE,
        related_name='pedido'
    )
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    empresa = models.CharField("Empresa", max_length=255)
    previsao_entrega = models.DateField("Previsão de Entrega", null=True, blank=True)
    data_recebimento = models.DateField("Data de Recebimento", null=True, blank=True)
    data_criacao = models.DateTimeField("Data do Pedido", auto_now_add=True)
    informacao = models.TextField("PO", blank=True, null=True) 

    def __str__(self):
        return f"Pedido #{self.pk} ({self.empresa})"
