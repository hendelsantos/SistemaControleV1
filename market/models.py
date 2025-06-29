from django.db import models

class ItemMarket(models.Model):
    nome = models.CharField(max_length=120)
    catalogo = models.CharField(max_length=40)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='market_fotos/')
    estoque = models.IntegerField(default=0)  # Opcional

    def __str__(self):
        return f"{self.nome} - {self.catalogo}"

class Requisicao(models.Model):
    nome_requisitante = models.CharField(max_length=80)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Requisição de {self.nome_requisitante} em {self.data:%d/%m/%Y}"

class ItemRequisitado(models.Model):
    requisicao = models.ForeignKey(Requisicao, on_delete=models.CASCADE, related_name='itens')
    item = models.ForeignKey(ItemMarket, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.item.nome}"
