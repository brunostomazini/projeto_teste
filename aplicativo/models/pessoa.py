from datetime import *

from django.db import models
from .base import Base
from django.core.exceptions import ValidationError

from ..enumerations import Genero

class Pessoa(Base):
    nome = models.CharField(default='',max_length=100, verbose_name='Nome', help_text='Nome da pessoa')
    data_nascimento = models.DateField(default=date.today(),verbose_name='Data de Nascimento', help_text='Data de Nascimento')
    genero = models.CharField(max_length=20, choices=Genero, default=Genero.NAO_ESPECIFICADO, verbose_name='Gênero')

    def __str__(self):
        return f"{self.nome} - ID:{self.id}"

    def clean(self):
        today = date.today()

        if self.data_nascimento > today:
            raise ValidationError("Data de nascimento invalida")
