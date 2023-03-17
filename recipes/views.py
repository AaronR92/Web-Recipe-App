from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from recipes.models import Recipe

def index(request):
    latest_recipe_list = Recipe.objects.order_by('-pub_date')[:5]
    output = ', '.join([recipe.name for recipe in latest_recipe_list])
    return HttpResponse(output)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return HttpResponse(recipe)
