from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from airline import user


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request,'users/user.html')

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'user/login.html',
                          {"message":"invalid credentials"})
    return render(request,"user/login,html")
def logout_request(request):
    logout(request)
    return render(request,"users/login.html",{
        "message":"logged out"
    })
