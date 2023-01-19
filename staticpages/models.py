from django.db import models

# Create your models here.

class Equipe(models.Model):
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    imagem_url = models.URLField(verbose_name="URL da Imagem de Perfil")
    descricao = models.TextField(verbose_name="Descrição", max_length=4097)
    ordem = models.IntegerField(default=0)
    def __str__(self):
        return self.nome