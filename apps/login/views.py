from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages



# Create your views here.
def splash (request):
    context={
    }
    return render(request, 'login/base.html', context)
def login_page (request):
    return render(request, 'login/login.html')

def login (request):
    results=User.objects.user_validate(request.POST)
    if results[0]:
        for error in results:
            messages.error(request, error, extra_tags='danger')
        return redirect ('login:login_page')
    else:

        request.session['user']={
        'id':results[1].id,
        'u_name':results[1].u_name
        }
        messages.success(request,"You logged in successfully")
    return redirect('recipes:splash')
def register(request):
    return render (request, 'login/register.html')
def create_user(request):

    errors= User.objects.reg_validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error, extra_tags='danger')
        return redirect('login:register')
    User.objects.create_user(request.POST)
    messages.success(request, 'Successfully registered!')
    user=User.objects.get(u_name=request.POST['u_name'].title())
    request.session['user']={
    'id':user.id,
    'u_name':user.u_name
    }
    return redirect('login:recipes')
def edit_user(request):
    changes=User.objects.edit_user(request.POST)
    if changes[0]:
        for error in changes:
            messages.error(request, error, extra_tags='danger')
        return redirect('recipes:myaccount')
    User.objects.filter(id=request.session['user']['id']).update(**changes[1])
    messages.success(request, 'successfully update user info.')
    return redirect('recipes:splash')
def logout(request):
    request.session.flush()
    messages.success(request, 'Successfully logged out!')
    return redirect('login:splash')
