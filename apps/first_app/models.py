from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length = 55)
    amount = models.IntegerField()
    measurement = models.CharField(max_length = 55)
    
class Tool(models.Model):  
    name = models.CharField(max_length = 55)
    amount = models.IntegerField()
    measurement = models.CharField(max_length = 55)

class Step(models.Model):  
    number = models.IntegerField()
    phrase = models.TextField()
    set_timer_amount = models.IntegerField(null=True, blank=True)
    # photo = models.ImageField(upload_to='steps/', null=True, blank=True)

class Recipe(models.Model):
    title = models.CharField(max_length = 55)
    description_1 = models.TextField(default='none')
    description_2 = models.TextField(default='none')
    time_to_cook = models.IntegerField()
    servings = models.IntegerField()
    cals_per_serv = models.IntegerField()
    main_photo = models.ImageField(upload_to='recipe_photos/')
    recipe_photo = models.ImageField(upload_to='recipe_photos/')
    total_steps = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient, related_name= "recipes")
    tools = models.ManyToManyField(Tool, related_name= "recipes")
    steps = models.ManyToManyField(Step, related_name= "recipes")
