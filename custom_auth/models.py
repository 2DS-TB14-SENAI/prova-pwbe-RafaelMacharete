from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Now

class CustomUser(AbstractUser):
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(birth_date__lt=Now()),
                name='data_nascimento_nao_pode_ser_em_datas_passadas'
            )
        ]

    phone = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    birth_date = models.DateField(blank=True, null=True)