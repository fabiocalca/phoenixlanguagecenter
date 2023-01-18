from django.db import models
from usuarios.models import Aluno, Professor
from website import settings
from django.db.models import F, Sum
from professores.models import Aula
from sortedm2m.fields import SortedManyToManyField

class Idioma(models.Model):
    id = models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=30)
    def __str__(self):
        return self.idioma

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=30, default='')
    ativo = models.BooleanField(default=True)
    idioma_do_curso = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    professor_do_curso = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    alunos_do_curso = SortedManyToManyField(Aluno)
    aulas_dadas = models.IntegerField(default=0)
    aulas_pagas = models.IntegerField(default=0)
    presenca = models.IntegerField(default=0)
    aulas_restantes = models.IntegerField(default=0)
    def __str__(self):
        return self.curso

class Pagamento(models.Model):
    id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    pago = models.BooleanField(default=False)
    valor = models.DecimalField(decimal_places=2, max_digits=6)
    aulas_no_pacote = models.IntegerField(default=0)
    data = models.DateField(auto_now_add=True, blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        aulas_pagas = Pagamento.objects.filter(curso=self.curso, pago=True).aggregate(total=Sum('aulas_no_pacote')).get('total',0)
        if not aulas_pagas:
            aulas_pagas = 0
        aulas_dadas = Aula.objects.filter(curso=self.curso).count()
        Curso.objects.filter(id=self.curso.id).update(aulas_restantes=aulas_pagas-aulas_dadas)
        
    def __str__(self):
        return ('#' + str(self.id) + ' ' + self.curso.curso)
