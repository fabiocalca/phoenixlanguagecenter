from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.CharField(max_length=30, blank=True)
    data_de_nascimento = models.DateField(null=True, blank=True)
    eh_aluno = models.BooleanField(default=False, verbose_name="Aluno")
    eh_professor = models.BooleanField(default=False, verbose_name="Professor")
    eh_empresa = models.BooleanField(default=False, verbose_name="Empresa")

class Professor(models.Model):
    class Meta:
        verbose_name_plural = 'professores'
    id = models.AutoField(primary_key=True)
    usuario_professor = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    descricao = models.TextField(max_length=4097, blank=True)
    def __str__(self):
        return self.usuario_professor.first_name

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_empresa = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30, blank=True)
    contrato_ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    class Meta:
        ordering = ['usuario_aluno__first_name', 'usuario_aluno__last_name']
    id = models.AutoField(primary_key=True)
    usuario_aluno = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    empresa_vinculada = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return (str(self.usuario_aluno.first_name) + ' (' + str(self.empresa_vinculada.nome + ')'))



