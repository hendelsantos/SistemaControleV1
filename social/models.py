from django.db import models

class Post(models.Model):
    nome = models.CharField("Nome", max_length=100)
    mensagem = models.TextField("Mensagem")
    imagem = models.ImageField("Foto", upload_to="social_fotos/", blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.criado_em:%d/%m/%Y %H:%M}"

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    nome = models.CharField("Nome", max_length=100)
    comentario = models.TextField("Comentário")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} em {self.post}"