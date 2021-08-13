from django.db import models
from django.db.models.fields import DateTimeField


class Deal(models.Model):
    username = models.CharField(max_length=255, verbose_name='username') 
    item = models.CharField(max_length=255, verbose_name='item')
    total = models.PositiveIntegerField(verbose_name='total')
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    date = DateTimeField(verbose_name='date')

    def __str__(self):
        return self.username