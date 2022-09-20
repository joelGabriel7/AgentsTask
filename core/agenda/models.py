import datetime
from time import strftime

from django.db import models
# from datetime import *
from datetime import datetime
from django.forms import model_to_dict

now = datetime.now()


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripcion')
    time_limits = models.DateTimeField(default=now, verbose_name='Fecha de ingreso')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item
