from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def reg(request):
    errors = Users.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value,extra_tags=key) 
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        user = Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash, confirm_password=pw_hash)
        messages.success(request,"Success Registartion")
        context = {'first_name': user.first_name}
        return render(request,"success.html",context)

def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        try:
            email = request.POST['email']
            user = Users.objects.get(email=email)
            return render(request, "success.html", {'first_name': user.first_name})
        except ObjectDoesNotExist:
            messages.error(request, "User not found", extra_tags='email')
            return redirect('/')
def user_logout(request):
    logout(request)
    return redirect('/') 