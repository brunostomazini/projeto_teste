from django.db import models

class Base(models.Model):

    class meta:
        abstract = True #Esta classe não cria objeto
        app_label = 'teste'