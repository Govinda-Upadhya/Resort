from django.shortcuts import render,redirect 
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import auth

# Create your views here.


def loginn(request):
    form = loginForm()

    if request.method == 'POST':
        form = loginForm(request.POST)

        
        username = request.POST.get('username')
        password = request.POST.get('password1')
        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            print(username)
            # Redirect or do something else after successful login
            return redirect('home')

    return render(request, 'login/login.html', {'form': form})
    
def signup(request):
    form=signUpForm()
    if request.method=='POST':
        form=signUpForm(request.POST)
        
        if form.is_valid():
            user=form.save()
            authenticated_user = authenticate(request, username=user.username, password=request.POST['password1'])
            if authenticated_user is not None:
                # Login the user
                login(request,authenticated_user)
                return redirect('home')
        else:
            print(form.errors)
    return render(request,'login/signup.html',{
        'form':form 
    })
def logout(request):
    if(request.method=="POST"):
        auth.logout(request)
        return redirect('home')
    return render(request,"login/logout.html")
