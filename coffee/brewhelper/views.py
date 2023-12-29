from django.shortcuts import render, HttpResponse
from .models import BrewStep
# Create your views here.

def home(request):
    steps = BrewStep.objects.all()

    target_total_water = 0
    target_total_time = 0

    for step in steps:
        target_total_water += step.change_in_water
        target_total_time += step.change_in_time
        step.target_total_time = target_total_time
        step.target_total_water = target_total_water

    return render(request, 'home.html', {'steps': steps})