from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-recipes', views.get_recipes, name='get_recipes'),
    path('user-guide/', views.user_guide, name='user_guide'),
]