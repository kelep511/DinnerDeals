from django.shortcuts import render, redirect, render_to_response
from . import init
from .models import Recipes, Ingredients
from ..login.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import Count
import json
import ast
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def first_time(request):
    if 'user' not in request.session:
        return redirect(request, 'login:')
    if not request.session['user']['id'] == 1:
        return redirect(reverse('recipes:splash'))
    init.replace()
    init.startup()
    print 'Initalization successful'
    messages.success(request, 'Successfully Initalized!')
    return redirect(reverse('recipes:splash'))

def new(request):
    return render(request, 'recipes:new.html')

def create_recipe(request):
    if not request.method == 'POST':
        return redirect(reverse('recipse:splash'))
    ingdata=[]
    unitdata=[]
    count=int(request.POST['hidden'])
    for i in range(1, count+1):
        ingdata.append(request.POST["item"+str(i)])
        unitdata.append({'qty': request.POST['qty'+str(i)],'unit': request.POST['unit'+str(i)]})
    recipe=Recipes.objects.newRecipe(request.POST, request.session['user']['id'],ingdata, unitdata)
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

def user(request, u_id):
    context={
    'user':User.objects.filter(id=u_id)[0],
    'recipes':Recipes.objects.filter(author=User.objects.filter(id=u_id)[0]).order_by('-created_at')
    }
    return render(request, 'recipes/user.html', context)
def view_recipe(request,r_id):
    context={
    'recipe':Recipes.objects.filter(id=r_id).annotate(tot_ing=Count('ingredients'))[0],
    'user':User.objects.filter(id=request.session['user']['id'])[0],
    }
    print context['recipe'].ingredients.all

    rep=context['recipe'].units
    rep=ast.literal_eval(rep)
    context.update({'rep':rep,})
    return render (request, 'recipes/view_recipe.html', context)
# def browse(request):
#     context={
#     'user':User.objects.filter(id=request.session['user']['id'])[0],
#     'recipes':Recipes.objects.exclude(isprivate=True).order_by('-created_at'),
#     'hot':Recipes.objects.exclude(isprivate=True).annotate(num_favs=Count('favorites')).order_by('-num_favs')[:5]
#     }
#     return render(request, "recipes/browse.html", context)
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
def browse(request):
    context={
    'user':User.objects.filter(id=request.session['user']['id'])[0],
    'hot':Recipes.objects.exclude(isprivate=True).annotate(num_favs=Count('favorites')).order_by('-num_favs')[:3]
    }
    recipe=Recipes.objects.exclude(isprivate=True).order_by('-created_at')


    paginator = Paginator(recipe, 2)
    page = request.GET.get('page')
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)

    context.update({'recipes':recipes,'page':page})

    return render(request, 'recipes/browse.html',context)
