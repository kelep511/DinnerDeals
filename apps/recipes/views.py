from django.shortcuts import render, redirect
from ..login.models import User
from . import init
from .models import Recipes, Ingredients
from ..login.models import User


# Create your views here.
def first_time(request):
    if 'id' not in request.session:
        return redirect(request, 'login:index')
    if not request.session['id'] == 1:
        return redirect(request, 'recipes:index')
    init.startup()
    print 'Initalization successful'
    return redirect(request, 'login:index')

def new(request):
    return render(request, 'recipes:new.html')

def create_recipe(request):
    ingdata=[]
    for item in request.POST['item']:
        ingdata.push(item)
    recipe=Recipe.objects.newRecipe(request.POST['title'], request.POST['desc'],ingdata)
    messages.success(request, recipe.title+' added successfully.')
    return redirect('recipes:add_recipe')

def splash(request):
    return render (request, 'recipes/splash.html')
def myaccount(request):
    context={
    'user':User.objects.get(id=request.session['user']['id'])
    }
    return render (request, 'recipes/myaccount.html', context)
def add_recipe(request):
    return render (request, 'recipes/add_recipe.html')
