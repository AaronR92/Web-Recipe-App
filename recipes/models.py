from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Direction(models.Model):
    direction = models.CharField(max_length=200)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=400)
    directions = models.ForeignKey(Direction, models.CASCADE)
    ingredients = models.ForeignKey(Ingredient, models.PROTECT)
