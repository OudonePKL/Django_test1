from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

# Create your views here.
@login_required(login_url='/')
def home(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request, 'signUp.html')

def login(request):
    return render(request, 'login.html')


# Authenticate

def addUser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    re_password = request.POST['re_password']

    if password == re_password:
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'This username is already exist!')
            return redirect('/signUp')
        elif CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'This email is already exist!')
            return redirect('/signUp')
        else:
            
            new_user = CustomUser(
                username = username,
                email = email,
                password = password,
                user_type = 2,
            )
            new_user.save()

            return redirect('/')
    else:
        messages.info(request, 'The password do not match!')
        return redirect('/signUp')

def signUpForm(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    re_password = request.POST['re_password']

    if password == re_password:
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'This username is already exist!')
            return redirect('/signUp')
        elif CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'This email is already exist!')
            return redirect('/signUp')
        else:
            
            new_user = CustomUser(
                username = username,
                email = email,
                password = password,
                user_type = 2,
            )
            new_user.save()

            return redirect('/')
    else:
        messages.info(request, 'The password do not match!')
        return redirect('/signUp')

def loginForm(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        user_type = user.user_type
        if user_type == 1:
            return HttpResponse('This Is Hod Panel')
        if user_type == 2:
            return HttpResponse('This Is Active Panel')
        # return redirect('/dashboard')
    else:
        messages.error(request, 'Not Found :(')
        return redirect('/')

def logOut(request):
    auth.logout(request)
    return redirect('/')

