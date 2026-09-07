from django.contrib import admin

# Register your models here.
from .models import Cake
from .models import Recipe

admin.site.register(Cake)
admin.site.register(Recipe) 