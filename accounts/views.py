from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(request):
    return HttpResponseRedirect('accounts/login')

def signup(request):
    return HttpResponse('signup')

def login(request):
    return HttpResponse('login')