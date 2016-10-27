from django.shortcuts import render, redirect
from . import init
from .models import Recipes, Ingredients
from ..login.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect

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



def new(request):
    return render(request, 'recipes:new.html')

def create_recipe(request):
    ingdata=[]
    for item in request.POST['item']:
        ingdata.append(item)
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
def user(request, u_id):
    context={
    'user':User.objects.filter(id=u_id)[0],
    'recipes':Recipes.objects.filter(author=User.objects.filter(id=u_id)[0]).order_by('-created_at')
    }
    return render(request, 'recipes/user.html', context)
def view_recipe(request,r_id):
    context={
    'recipe':Recipes.objects.filter(id=r_id)[0],
    'user':User.objects.filter(id=request.session['user']['id'])[0],
    }
    return render (request, 'recipes/view_recipe.html', context)
def buttons(request, button, r_id):
    recipe= Recipes.objects.filter(id=r_id)[0]
    if button=='1':
        recipe.favorites.add(User.objects.get(id=request.session['user']['id']))
        messages.success(request,'Successfully added to favorites')
    elif button=='2':
        recipe.favorites.remove(User.objects.get(id=request.session['user']['id']))
        messages.success(request,'Successfully removed from favorites')
    elif button=='3':
        recipe.isprivate='True'
        recipe.save()
        messages.success(request,'Successfully made recipe private.')
    elif button=='4':
        recipe.isprivate='False'
        recipe.save()
        messages.success(request,'Successfully made recipe public.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
