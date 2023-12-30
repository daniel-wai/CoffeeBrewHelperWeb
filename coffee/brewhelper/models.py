from django.db import models

# Create your models here.
class BrewStep(models.Model):
    step_id = models.PositiveIntegerField()
    description = models.CharField(max_length=200, default='')
    change_in_water = models.IntegerField()
    change_in_time = models.IntegerField()

    recipeID = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='steps', null=True)  # ForeignKey to Recipe

    def __str__(self):
        return f'Step {self.step_id}'

    class Meta:
        ordering = ['step_id']  # Choose a field for default ordering

class Recipe(models.Model):
    recipe_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    temperature = models.PositiveIntegerField(default=95)
    coffee_weight = models.PositiveIntegerField(default=0)
    coffee_grind_size = models.TextField(default='')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['recipe_id']  # Choose a field for default ordering

class BrewMethod(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe, related_name='methods')