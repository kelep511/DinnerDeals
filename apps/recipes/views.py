from django.shortcuts import render, redirect
from ..login.models import User

# Create your views here.
def splash(request):
    return render (request, 'recipes/splash.html')
def myaccount(request):
    context={
    'user':User.objects.get(id=request.session['user']['id'])
    }
    return render (request, 'recipes/myaccount.html', context)
def add_recipe(request):
    return render (request, 'recipes/add_recipe.html')
def create_recipe(request):
    print'*'*50
    print request.POST
    print'*'*50
    return redirect('recipes:add_recipe')
