from django.db import models

# Create your models here.

# Equipment used for carry out a method
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

# Method of making coffee
class BrewMethod(models.Model):
    name = models.CharField(max_length=100)
    equipment = models.ManyToManyField(Equipment, related_name='brewmethods')

    def __str__(self):
        return self.name

# Collection of steps to make coffee which may be considered one or more method types
class Recipe(models.Model):
    methods = models.ManyToManyField(BrewMethod, related_name='recipes')

    recipe_id = models.PositiveIntegerField()
    name = models.CharField(max_length=150, default='')
    description = models.TextField(default='')
    reference = models.TextField(default='')
    temperature = models.TextField(default='')
    coffee_weight = models.PositiveIntegerField(default=0)
    coffee_grind_size = models.TextField(default='')   
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['recipe_id']  # Choose a field for default ordering

# General step to complete a recipe
class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps', null=True)  # ForeignKey to Recipe
    
    step_id = models.PositiveIntegerField()
    description = models.TextField(default='')

    def has_brewstep(self):
        return hasattr(self, 'brewstep')

    def __str__(self):
        return f'Step {self.step_id}'

    class Meta:
        ordering = ['step_id']  # Choose a field for default ordering

# Time sensitive step where water is added to coffee for flavour extraction
class BrewStep(models.Model):
    step = models.OneToOneField(Step, on_delete=models.CASCADE, primary_key=True)

    brew_step_id = models.PositiveIntegerField()
    change_in_water = models.IntegerField()
    change_in_time = models.IntegerField()
   
    def __str__(self):
        return f'BrewStep {self.brew_step_id}'
    
    class Meta:
        ordering = ['brew_step_id']  # Choose a field for default ordering

