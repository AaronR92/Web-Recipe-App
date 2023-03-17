import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=400)

    def __str__(self) -> str:
        return f'{self.name} - {self.category}'
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Direction(models.Model):
    direction = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, models.PROTECT, default=None)

    def __str__(self) -> str:
        return self.direction
    

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, models.PROTECT, default=None)

    def __str__(self) -> str:
        return self.name
    