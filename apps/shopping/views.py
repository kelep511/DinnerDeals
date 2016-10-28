from django.shortcuts import render, redirect
from django.http import HttpResponse
from xml.dom.minidom import parse, parseString
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from ..login.models import User
from ..recipes.models import Recipes, Ingredients
from json import dumps
import json
import requests
import re
import xml.etree.cElementTree as et
# Create your views here.

def idCheck(request):
    if 'user' not in request.session:
        messages.add_message(request, messages.ERROR, 'Please login to continue.')
        return False
    else:
        return True

def search(request):
    idCheck(request)
    if 'zip' not in request.session:
        user=User.objects.get(id=request.session['user']['id'])
        request.session['zip']=user.z_code
    return render(request, 'shopping/search.html')

def multi(request):
    pass

def displaysingle(request):
    r_id=request.POST['recipes']
    print r_id
    recipe=Recipes.objects.filter(id=r_id)[0]
    context=[]
    title=recipe.title+'|'
    context.append(title)
    print context
    fullingredients=Ingredients.objects.filter(recipe_ing=recipe)
    for items in fullingredients:
        context.append(items.name+' | ')
        context.append(items.itemid+' | ')
        if items.itemid == 'NOITEM':
            context.append(' A water tap | ')
            context.append(' You have water at home, right? | ')
        else:
            url='http://www.SupermarketAPI.com/api.asmx/SearchForItem?APIKEY=6af0d05f87&StoreId='+request.session['storeid']+'&ItemName='+items.itemid
            product=requests.get(url).content
            product=re.sub(' xmlns="[^"]+"', '', product, count=1)
            product=dumps(bf.data(fromstring(product)))
            pdata=json.loads(product)
            print pdata
            print pdata['ArrayOfProduct']['Product']['AisleNumber']['$']
            print pdata['ArrayOfProduct']['Product']['ItemCategory']['$']
            context.append(pdata['ArrayOfProduct']['Product']['AisleNumber']['$'] + ' |')
            context.append(pdata['ArrayOfProduct']['Product']['ItemCategory']['$'] + ' |')
    return HttpResponse(context)

def zipsearch(request):
    request.session['zip']=request.POST['zip']
    zipp=request.POST['zip']
    stores={}
    url='http://www.SupermarketAPI.com/api.asmx/StoresByZip?APIKEY=6af0d05f87&ZipCode='+str(zipp)
    stores=requests.get(url).content
    stores=re.sub(' xmlns="[^"]+"', '', stores, count=1)
    stores=dumps(bf.data(fromstring(stores)))

    return HttpResponse(stores)

def store(request):
    idCheck(request)
    if not request.POST and 'storeid' not in request.session:
        return redirect(reverse('shop:search'))
    if 'storeid' not in request.session:
        request.session['storeid']=request.POST['storeid']
    context={
    'storeid':request.session['storeid'],
    'recipes':Recipes.objects.filter(author=User.objects.get(id=request.session['user']['id'])),
    }
    return render(request, 'shopping/singleshop.html', context)
