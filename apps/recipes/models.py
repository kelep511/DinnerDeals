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
    def newRecipe(self,postdata, u_id, ingdata, unitdata):
        if postdata['dire'] == '' and postdata['desc'] == '':
            recipe=Recipes.objects.create(title=str(postdata["title"]),units=unitdata, author=User.objects.get(id=u_id))
        elif postdata['dire'] == '':
            recipe=Recipes.objects.create(title=str(postdata["title"]),units=unitdata, author=User.objects.get(id=u_id),desc=postdata['desc'])
        elif postdata['desc'] == '':
            recipe=Recipes.objects.create(title=str(postdata["title"]),units=unitdata, author=User.objects.get(id=u_id), dire=postdata['dire'])
        else:
            recipe=Recipes.objects.create(title=str(postdata["title"]),units=unitdata, author=User.objects.get(id=u_id), dire=postdata['dire'] ,desc=postdata['desc'])
        print ingdata
        for item in ingdata:
            print item
            item=re.sub("u'"," ",item)
            ing=Ingredients.objects.get(name=str(item))
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
    units=models.TextField(default="{ 'ing': 'Nothing?', 'qty': 'Nothing', 'unit':'Nothing' }")
    top_favorites=models.ManyToManyField('login.User', related_name='top_favs')
    isprivate=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=RecipeManager()

class Ingredients(models.Model):
    name=models.CharField(max_length=100)
    itemid=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=IngredientManager()
