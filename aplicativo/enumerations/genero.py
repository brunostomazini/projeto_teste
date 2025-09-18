from django.db import models

class Genero(models.TextChoices):
    MALE = 'Masculino'
    FEMALE = 'Feminino'
    OTHER = 'Outros'
    NAO_ESPECIFICADO = "NAO ESPECIFICADO"