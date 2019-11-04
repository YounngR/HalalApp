from django.shortcuts import render
from .models import *



def main(request):

    return render(request, 'halalapp/main.html')

def goods(request):

    return render(request, 'halalapp/goods.html')

def recipe(request):

    return render(request, 'halalapp/recipe.html')

def event(request):

    return render(request, 'halalapp/event.html')

def recipe_registration(request):

    return render(request, 'halalapp/recipe_registration.html')

def login(request):

    return render(request, 'halalapp/login.html')
    
def Sign_up(request):

    return render(request, 'halalapp/Sign_Up.html')
