from django.shortcuts import render
from .models import Cake

# Create your views here.
def index(request):
    """The homepage."""
    return render(request, 'cake_recipes/index.html')


def links(request):
    """A base with links to the cakes and their recipes."""
    return render(request, 'cake_recipes/links.html')


def recipes(request):
    """A template for the recipes."""
    recipes = Cake.objects.all()
    context = {'recipes': recipes}
    return render(request, 'cake_recipes/recipes.html', context)


def recipe(request, recipe_id):
    """To show the individual cakes."""
    recipe = Cake.objects.get(id=recipe_id)
    recipe_items = recipe.recipe_set.all()
    context = {
        'recipe': recipe,
        'recipe_items': recipe_items,
    }
    return render(request, 'cake_recipes/recipe.html', context) 