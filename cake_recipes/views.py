from django.shortcuts import render
from .models import Cake

# Create your views here.
def index(request):
    """The homepage."""
    return render(request, 'cake_recipes/index.html')


def base(request):
    """A base with to the cakes and the homepage."""
    return render(request, 'cake_recipes/base.html')


def recipes(request):
    """Get all the cakes and make a template."""
    recipes = Cake.objects.all()
    context = {'recipes': recipes}
    return render(request, 'cake_recipes/recipes.html', context)


def recipe(request, recipe_id):
    """Show the individual recipes for the cakes."""
    recipe = Cake.objects.get(id=recipe_id)
    recipe_items = recipe.recipe_set.all()
    context = {
        'recipe': recipe,
        'recipe_items': recipe_items,
    }
    return render(request, 'cake_recipes/recipe.html', context) 