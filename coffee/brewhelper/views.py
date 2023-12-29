from django.shortcuts import render, HttpResponse
from .models import BrewStep, Recipe
# Create your views here.

def home(request):
    # Get the first Recipe instance
    recipe = Recipe.objects.first()

    # Get associated steps
    steps = recipe.steps.all().order_by('step_id')

    target_total_water = 0
    target_total_time = 0

    for step in steps:
        target_total_water += step.change_in_water
        target_total_time += step.change_in_time
        step.target_total_time = target_total_time
        step.target_total_water = target_total_water

    return render(request, 'home.html', {'recipe':recipe,'steps': steps})