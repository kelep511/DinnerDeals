from django.shortcuts import render, redirect
from ..login.models import User
from . import init
from .models import Recipes, Ingredients
from ..login.models import User
from django.contrib import messages

# Create your views here.
def first_time(request):
    if 'user' not in request.session:
        return redirect(request, 'login:')
    if not request.session['user']['id'] == 1:
        return redirect(reverse('recipes:splash'))
    if not request.inital:
        request.inital=1
        init.startup()
        print 'Initalization successful'
        messages.success(request, 'Successfully Initalized!')
        return redirect(reverse('recipes:splash'))
    if request.inital == 1:
        return redirect(reverse('recipes:splash'))

def user(request, u_id):
    context={
    'user':User.objects.filter(id=u_id)[0],
    }
    return render(request, 'recipes/user.html')

def new(request):
    return render(request, 'recipes:new.html')

def create_recipe(request):
    ingdata=[]
    for item in request.POST['item']:
        ingdata.push(item)
    recipe=Recipes.objects.newRecipe(request.POST['title'], request.session['user']['id'], request.POST['desc'],ingdata)
    messages.success(request, request.POST['title']+' added successfully.')
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
