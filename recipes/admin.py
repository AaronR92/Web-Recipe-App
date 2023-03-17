from django.contrib import admin

from recipes.models import Recipe, Direction, Ingredient, Category

class DirectionInline(admin.StackedInline):
    model = Direction
    extra = 1

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["name"]}),
        (None, {'fields': ['category']}),
        ('Publication date', {'fields': ['pub_date']}),
    ]
    inlines = [IngredientInline, DirectionInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)