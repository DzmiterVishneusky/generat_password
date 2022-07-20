from django.shortcuts import render
from django.http import HttpResponse
from random import *

# Create your views here.

def home(request):
    return render(request, 'generetor/home.html')

def info(request):
    return render(request, 'generetor/info.html') 

def password(request):

    chars = list('abcdefghijklmnopqrstuvwxyz')
    chars_trash = 'il1Lo0O'

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))
    if request.GET.get('special'):
        chars.extend(list('!#$%&*+-=?@^_'))
    if request.GET.get('trash'):
        for i in chars_trash:
            if i in chars:
                chars.remove(i)

    lenght = int(request.GET.get('lenght', 12))
    thepassword = ''

    for _ in range(lenght):
        thepassword += choice(chars)

    return render(request, 'generetor/password.html', {'password':thepassword})
