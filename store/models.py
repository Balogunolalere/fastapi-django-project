from datetime import datetime
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    price = models.FloatField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(max_length=200,unique=True, allow_unicode=True, verbose_name='slug')
    timestamp = models.DateTimeField(verbose_name='timestamp', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

