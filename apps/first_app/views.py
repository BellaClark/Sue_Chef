from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'first_app/index.html')

def recipe_page(request):
    return render(request, 'first_app/recipe-page.html')

def add_recipe(request):
    return render(request, 'first_app/add_recipe.html')

def about(request):
    return render(request, 'first_app/about.html')

def ingredients(request):
    return render(request, 'first_app/ingredients.html')