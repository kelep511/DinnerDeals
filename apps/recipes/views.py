from django.shortcuts import render
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
