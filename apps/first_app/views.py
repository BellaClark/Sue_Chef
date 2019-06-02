from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import *
import math

def index(request):
    variables = {
        'recipes' : Recipe.objects.all(),
    }
    return render(request, 'first_app/index.html', variables)

def recipe_page(request, recipe_id):
    variables = {
        'recipe' : Recipe.objects.get(id = recipe_id),
    }
    return render(request, 'first_app/recipe-page.html', variables)

def add_recipe(request):
    return render(request, 'first_app/add_recipe.html')

def about(request):
    return render(request, 'first_app/about.html')

def ingredients(request, recipe_id):
    variables = {
        'ingredients' : Recipe.objects.get(id = recipe_id).ingredients.all(),
        'recipe' : Recipe.objects.get(id = recipe_id),
    }
    return render(request, 'first_app/ingredients.html', variables)

def tools(request, recipe_id):
    variables = {
        'tools' : Recipe.objects.get(id = recipe_id).tools.all(),
        'recipe' : Recipe.objects.get(id = recipe_id),
    }
    return render(request, 'first_app/tools.html', variables)

def step(request, recipe_id, step_num):
    if step_num == "2" :
        print("step_num")
        return redirect("/tools/{}".format(recipe_id))
    else :
        if step_num == str(int(Recipe.objects.get(id = recipe_id).total_steps) + 1) :
            return redirect("/end_recipe/{}".format(recipe_id))
        else :
            variables = {
               'step' : Recipe.objects.get(id = recipe_id).steps.get(number=step_num),
               'recipe' : Recipe.objects.get(id = recipe_id),
            }
            return render(request, 'first_app/step.html', variables)
    return render(request, 'first_app/step.html')

def create_recipe(request, methods='POST'):
    errors = []
    if len(request.POST["title"]) < 1:
        errors.append("You must enter a title")

    if len(request.POST["description_1"]) < 1:
        errors.append("You must enter a description one")

    if len(request.POST["description_2"]) < 1:
        errors.append("You must enter a description two")

    if len(request.POST["time_to_cook"]) < 1:
        errors.append("You must enter a time to cook")
    
    if len(request.POST["servings"]) < 1:
        errors.append("You must enter the number of servings")

    if len(request.POST["cals_per_serv"]) < 1:
        errors.append("You must enter the cals per serv")

    if not 'main_photo' in request.FILES:
        errors.append("You must upload a main photo")

    if not 'recipe_photo' in request.FILES:
        errors.append("You must upload a recipe photo")
    
    if len(request.POST["total_steps"]) < 1:
        errors.append("You must enter the number of total steps")

    try:
        Recipe.objects.filter(title = request.POST["title"])[0]
        messages.error(request, 'This recipe title is already taken')
    except:
        this_title = request.POST["title"]
        this_description_1 = request.POST["description_1"]
        this_description_2 = request.POST["description_2"]
        this_time_to_cook = request.POST["time_to_cook"]
        this_servings = request.POST["servings"]
        this_cals_per_serv = request.POST["cals_per_serv"]
        if request.method == 'POST' and 'main_photo' in request.FILES:
            this_main_photo = request.FILES["main_photo"]
        if request.method == 'POST' and 'recipe_photo' in request.FILES:
            this_recipe_photo = request.FILES["recipe_photo"]
        this_total_steps = int(request.POST["total_steps"]) + 2

        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            new_recipe = Recipe.objects.create(title = this_title, description_1 = this_description_1, description_2 = this_description_2, time_to_cook = this_time_to_cook, servings = this_servings, cals_per_serv = this_cals_per_serv, main_photo = this_main_photo, recipe_photo = this_recipe_photo, total_steps = this_total_steps)
            return redirect("/add_ingredients/{}".format(new_recipe.id))
    return redirect("/add_recipe")

def add_ingredients(request, recipe_id):
    variables = {
        'recipe' : Recipe.objects.get(id = recipe_id),
    }
    return render(request, 'first_app/add_ingredients.html', variables)

def create_ingredient(request, recipe_id):
    errors = []
    if len(request.POST["name"]) < 1:
        errors.append("You must enter a name")
    
    if len(request.POST["amount"]) < 1:
        errors.append("You must enter an amount")

    if len(request.POST["measurement"]) < 1:
        errors.append("You must enter a measurement or a blank space if NA")

    try:
        i = Ingredient.objects.filter(name = request.POST["name"], amount = request.POST["amount"], measurement = request.POST["measurement"])[0]
        r = Recipe.objects.get(id = recipe_id)
        r.ingredients.add(i)
        r.save()
    except:
        this_name = request.POST["name"]
        this_amount = request.POST["amount"]
        this_measurement = request.POST["measurement"]

        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            new_ingredient = Ingredient.objects.create(name = this_name, amount = this_amount, measurement = this_measurement)

            r = Recipe.objects.get(id = recipe_id)
            r.ingredients.add(new_ingredient)
            r.save()
            print("created and added ingredient!")
            return redirect("/add_ingredients/{}".format(recipe_id))
    return redirect("/add_ingredients/{}".format(recipe_id))
    
def add_tools(request, recipe_id):
    variables = {
        'recipe' : Recipe.objects.get(id = recipe_id),
    }
    return render(request, 'first_app/add_tools.html', variables)

def create_tool(request, recipe_id):
    errors = []
    if len(request.POST["name"]) < 1:
        errors.append("You must enter a name")
    
    if len(request.POST["amount"]) < 1:
        errors.append("You must enter an amount")

    if len(request.POST["measurement"]) < 1:
        errors.append("You must enter a measurement or a blank space if NA")

    try:
        i = Tool.objects.filter(name = request.POST["name"], amount = request.POST["amount"], measurement = request.POST["measurement"])[0]
        r = Recipe.objects.get(id = recipe_id)
        r.tools.add(i)
        r.save()
    except:
        this_name = request.POST["name"]
        this_amount = request.POST["amount"]
        this_measurement = request.POST["measurement"]

        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            new_tool = Tool.objects.create(name = this_name, amount = this_amount, measurement = this_measurement)

            r = Recipe.objects.get(id = recipe_id)
            r.tools.add(new_tool)
            r.save()
            print("created and added tool!")
            return redirect("/add_tools/{}".format(recipe_id))
    return redirect("/add_tools/{}".format(recipe_id))

def add_steps(request, recipe_id):
    variables = {
        'recipe' : Recipe.objects.get(id = recipe_id),
    }
    return render(request, 'first_app/add_steps.html', variables)

def create_step(request, recipe_id):
    errors = []
    if len(request.POST["step_num"]) < 1:
        errors.append("You must enter a step number")
    
    if len(request.POST["phrase"]) < 1:
        errors.append("You must enter a phrase")

    if len(request.POST["set_timer_amount"]) < 1:
        errors.append("You must enter a timer amount - if there is none just write 0")

    try:
        Step.objects.filter(number = int(request.POST["step_num"]) + 2, phrase = request.POST["phrase"], set_timer_amount = request.POST["set_timer_amount"])[0]
        messages.error(request, 'This step already exists')
    except:
        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            this_number = int(request.POST["step_num"]) + 2
            this_phrase = request.POST["phrase"]
            this_set_timer_amount = request.POST["set_timer_amount"]
            new_step = Step.objects.create(number = this_number, phrase = this_phrase, set_timer_amount = this_set_timer_amount)
            r = Recipe.objects.get(id = recipe_id)
            r.steps.add(new_step)
            r.save()
            print("created and added step!")
            return redirect("/add_steps/{}".format(recipe_id))
    return redirect("/add_steps/{}".format(recipe_id))

def end_recipe(request, recipe_id):
    variables = {
        'recipe' : Recipe.objects.get(id = recipe_id),
    }
    return render(request, 'first_app/finished_recipe.html', variables)
