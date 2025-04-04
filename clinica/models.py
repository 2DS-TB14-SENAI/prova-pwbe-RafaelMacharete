from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db.models.functions import Now

class Medico(models.Model):
    choices = [
        ('CAR', 'Cardiologista'),
        ('PSI', 'Psiquiatra')]

    def formatador(valor):
        try:
            int(valor[0:2])
            int(valor[3:8])
            if '/' is not valor[2]:
              print('oi')
              raise ValidationError('Não segue o formato necessário (XX-XXXXX)')
        except ValueError:
              raise ValidationError('Não segue o formato necessário (XX-XXXXX)')
        
    nome = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    especialidade = models.CharField(max_length=30, choices=choices)
    crm = models.CharField(max_length=8, unique=True, validators=[formatador])
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(data__gte=Now()),
                name='consulta_nao_pode_ser_em_datas_passadas'
            )
        ]

    choices = [
        ('agendado', 'agendado'),
        ('realizado', 'realizado'),
        ('cancelado', 'cancelado')
        ]
    
    paciente = models.CharField(max_length=50)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=choices)

    def __str__(self):
        return f'{self.paciente} - {self.medico}'