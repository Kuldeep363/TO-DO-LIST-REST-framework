from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .serializers import userSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from .forms import userForm
# Create your views here.

def home(request):
    return HttpResponseRedirect('accounts/login')

def signup(request):
    return render(request,'accounts/signup.html')
def logoutS(request):
    logout(request)
    return HttpResponseRedirect('login')
def loginS(request):
    error = ' '
    if request.method == "POST":
        form = userForm(request.POST)
        print(form.data['username'])
        username = form.data['username']
        password = form.data['password']
        user = authenticate(username = username,password = password)
        print(user)
        if user:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'accounts/login.html',{'error':'username and password does not match'})
    else:
        return render(request,'accounts/login.html',{'error':error})

@api_view(['GET'])
def userS(request):
    data = request.GET.get('username',None)
    try:
        User.objects.get(username = data)
    except User.DoesNotExist:
        return Response({'msg':''})

    return Response({'msg':'Username not available'})
    
@api_view(['POST'])
def signupS(request):
    data = request.data
    print(data)
    user = User(username = data['username'])
    user.set_password(data['password'])
    user.save()
    return Response({'success':'done'})
    

# @api_view(['POST'])
# def loginS(request):
#     try:
