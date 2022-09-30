from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def home(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request, 'signUp.html')

def login(request):
    return render(request, 'login.html')


# Authenticate
def signUpForm(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    re_password = request.POST['re_password']

    if password == re_password:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'This username is already exist!')
            return redirect('/signUp')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'This email is already exist!')
            return redirect('/signUp')
        else:
            new_user = User.objects.create_user(
                username = username,
                email = email,
                password = password,
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
        return redirect('/dashboard')
    else:
        messages.error(request, 'Not Found :(')
        return redirect('/')

def logOut(request):
    auth.logout(request)
    return redirect('/')

