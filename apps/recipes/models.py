from __future__ import unicode_literals
from ..login.models import User
from django.db import models
import re

# Create your models here.

class IngredientManager(models.Manager):
    def addIngredient(self,i_name,i_id):
        Ingredients.objects.create(name=i_name,itemid=i_id)
        return True

# In order to add ingredients to recipe, must pass an array of product ids
class RecipeManager(models.Manager):
    def newRecipe(self,postdata, u_id, ingdata):
        recipe=Recipes.objects.create(title=str(postdata["title"]),author=User.objects.get(id=u_id), dire=postdata['dire'] ,desc=postdata['desc'])
        # ingdata=ingdata.join([str(x) for x in ingdata])
        # ingdata=ingdata.split(',')
        print ingdata
        for item in ingdata:
            print item
            ing=Ingredients.objects.filter(itemid=int(item))[0]
            # Try changing to objects.get_or_create()
            recipe.ingredients.add(ing)
            recipe.save()
        if 'private' in postdata:
            recipe.isprivate=True
            recipe.save()
        return True
    def deleteRecipe(self,r_id):
        Recipes.objects.get(id=r_id).delete()
        return True
    def updateRecipe(self,r_id,formdata,ingdata):
        recipe=Recipes.objects.get(id=r_id)
        recipe.title=data.title
        recipe.ingredients={}
        for item in ingdata:
            ing=Ingredients.objects.get(itemid=item)
            recipe.ingredients.add(ing)
            recipe.save()
        return True

class Recipes(models.Model):
    title=models.CharField(max_length=40)
    author=models.ForeignKey('login.User', related_name='recipe_author')
    ingredients=models.ManyToManyField('Ingredients', related_name='recipe_ing')
    desc=models.TextField(default='No discription entered.')
    dire=models.TextField(default='Throw it together and hope for the best.')
    favorites=models.ManyToManyField('login.User', related_name='favs')
    isprivate=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=RecipeManager()

class Ingredients(models.Model):
    name=models.CharField(max_length=40)
    itemid=models.CharField(max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=IngredientManager()
