from django.shortcuts import render, redirect
import requests

# Create your views here.

def search(request):
    return render(request, 'shopping/search.html')

def zipsearch(request):
    zipp=request.POST['zip']
    url='http://www.SupermarketAPI.com/api.asmx/StoresByZip?APIKEY=6af0d05f87&ZipCode='+str(zipp)
    response=requests.get(url)
    for items in response:
        print items
    return response
