from django.shortcuts import render, redirect
from django.http import HttpResponse
from xml.dom.minidom import parse, parseString
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps
import requests
import re
# Create your views here.

def idCheck(request):
    if 'id' not in request.session:
        messages.add_message(request, messages.ERROR, 'Please login to continue.')
        return False
    else:
        return True

def search(request):
    if 'data' not in request.session:
        return render(request, 'shopping/search.html')
    context={
    'data':request.session['data'],
    }
    return render(request, 'shopping/search.html', context)

def multi(request):
    pass

def zipsearch(request):
    request.session['data']=''
    request.session['zip']=request.POST['zip']
    zipp=request.POST['zip']
    stores={}
    url='http://www.SupermarketAPI.com/api.asmx/StoresByZip?APIKEY=6af0d05f87&ZipCode='+str(zipp)
    stores=requests.get(url).content
    stores=re.sub(' xmlns="[^"]+"', '', stores, count=1)
    stores=dumps(bf.data(fromstring(stores)))
    return HttpResponse(stores)

def store(request):
    if not request.POST:
        return redirect(reverse('shop:search'))

    context={
    'storeid':request.POST['storeid'],
    }
    return render(request, 'shopping/singleshop.html', context)
