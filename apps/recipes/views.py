from django.shortcuts import render
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

def create(request):
    ingdata=[]
    # Push data to ingdata from request.post object. Determine total number of ingredients then iterate through with for loop to push all of them.
    recipe=Recipe.objects.newRecipe(request.POST['title'], request.POST['desc'],ingdatas)
    messages.success(request, recipe.title+' added successfully.')
    return True
