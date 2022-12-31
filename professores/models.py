from django.db import models
from usuarios.models import Professor
import django
from django.db.models import F, Sum
import adm.models
# Create your models here.

class Aula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255, default='Título da Aula')
    descricao = models.TextField(verbose_name="Descrição", max_length=500, default='Descricao')
    curso = models.ForeignKey('adm.Curso', on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING, default=None)
    presente = models.BooleanField(default=False)
    data = models.DateTimeField(default=django.utils.timezone.now)
    def save(self, *args, **kwargs):
        aulas_pagas = adm.models.Pagamento.objects.filter(curso=self.curso,pago=True).aggregate(total=Sum('aulas_no_pacote')).get('total',0)
        aulas_dadas = Aula.objects.filter(curso=self.curso).count()
        presenca = Aula.objects.filter(curso=self.curso, presente=True).count()
        adm.models.Curso.objects.filter(id=self.curso.id).update(aulas_restantes=aulas_pagas-aulas_dadas, presenca=presenca, aulas_dadas=aulas_dadas)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return (self.curso.curso + str(self.data))