from django.db import models
from django.urls.base import reverse_lazy


class Hero(models.Model):
    name = models.CharField(max_length=100, default='name')
    identity = models.CharField(max_length=100, default='identity')
    description = models.TextField(default='description')
    weakness = models.CharField(max_length=100, default='weakness')
    strength = models.CharField(max_length=100, default='strength')
    image = models.CharField(max_length=100, default='link to image')

    def __str__(self):
        return f'{self.name}, Alias: {self.identity}, Description: {self.description}'

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])

# Create your models here.
