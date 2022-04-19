from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='user-login')
def user(request):
    return render(request, 'dashboard/user.html')   

@login_required(login_url='user-login')
def business(request):
    return render(request, 'dashboard/business.html')

@login_required(login_url='user-login')
def neighbourhood(request):
    return render(request, 'dashboard/neighbourhood.html')    