from django.db import models
from django.forms import CharField
from .pessoa import Pessoa

from .base import Base

class Carro(Base):
    modelo=CharField(max_length=20)
    dono=models.ForeignKey(Pessoa, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.modelo} - {self.dono}'
