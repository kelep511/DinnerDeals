from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


# Create your views here.
def splash (request):
    context={
    }
    return render(request, 'login/base.html', context)
