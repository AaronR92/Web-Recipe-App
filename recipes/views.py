from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from recipes.models import Recipe, Ingredient

class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        """
        Return the last five published recipes (not including those set to be
        published in the future).
        """
        return Recipe.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

    def get_queryset(self):
        """
        Excludes any recipes that aren't published yet. 
        """
        return Recipe.objects.filter(pub_date__lte = timezone.now())


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return HttpResponse(recipe)
