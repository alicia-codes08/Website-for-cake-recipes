from django.urls import path
from . import views

app_name = 'cake_recipes'
urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    path('recipes/', views.recipes, name='recipes'),
    # Individual recipes
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'), 
]