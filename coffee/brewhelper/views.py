from django.shortcuts import render, HttpResponse
from .models import brewstep
# Create your views here.

def home(request):
    steps = brewstep.objects.all()

    total_water = 0
    total_time = 0

    for step in steps:
        total_water += step.change_in_water
        total_time += step.change_in_time
        step.total_time = total_time
        step.total_water = total_water

    return render(request, 'home.html', {'steps': steps})