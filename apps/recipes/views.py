from django.shortcuts import render, redirect
from ..login.models import User
from . import init
from .models import Recipes, Ingredients
from ..login.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def first_time(request):
    if 'user' not in request.session:
        return redirect(request, 'login:')
    if not request.session['user']['id'] == 1:
        return redirect(reverse('recipes:splash'))
    init.startup()
    print 'Initalization successful'
    messages.success(request, 'Successfully Initalized!')
    return redirect(reverse('recipes:splash'))


def user(request, u_id):
    user=User.objects.filter(id=u_id)[0]
    print user.id
    context={
    'user':user,
    'recipes':Recipes.objects.filter(author=user),
    }
    print context['user'].u_name
    return render(request, 'recipes/user.html', context)

def new(request):
    return render(request, 'recipes:new.html')

def create_recipe(request):
    if not request.method == 'POST':
        return redirect(reverse('recipse:splash'))
    ingdata=[]
    count=int(request.POST['hidden'])
    for i in range(1, count+1):
        ingdata.append(request.POST["item"+str(i)])
    recipe=Recipes.objects.newRecipe(request.POST, request.session['user']['id'],ingdata)
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
    context={
    'ingredients':Ingredients.objects.distinct().order_by('name'),
    }
    return render (request, 'recipes/add_recipe.html', context)
