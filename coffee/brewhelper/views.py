from django.shortcuts import render, HttpResponse
from .models import BrewStep, Recipe
# Create your views here.

def home(request):
    recipes = Recipe.objects.all()
    selected_recipe = None
    steps = []

    if 'selected_recipe_id' in request.GET:
        # Get recipe
        selected_recipe_id = request.GET['selected_recipe_id']
        try:
            selected_recipe = Recipe.objects.get(id=selected_recipe_id)
            # Get associated steps
            steps = selected_recipe.steps.all().order_by('step_id')
            order_id = 1
            target_total_water = 0
            target_total_time = 0

            for step in steps:
                step.order_id = order_id
                order_id += 1
                target_total_water += step.change_in_water
                target_total_time += step.change_in_time
                step.target_total_time = target_total_time
                step.target_total_water = target_total_water
            
            selected_recipe.target_total_time = target_total_time
            selected_recipe.target_total_water = target_total_water
            # Calculate brew ration assuming that water density is 1 g/mL
            selected_recipe.brew_ratio = "{:.1f}".format(selected_recipe.target_total_water/selected_recipe.coffee_weight) 
                
        except:
            pass #do not render any recipe info if selected_recipe = None

    return render(request, 'home.html', {'recipes': recipes, 'selected_recipe': selected_recipe, 'steps': steps})
