from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')
def password(request):
    characters = list('abcdefghklmnoprstxyz')
    if request.GET.get('UpperCase'):
        characters.extend(list('ABCDEFGHKLMNOPTSRXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    print(characters)
    lenght = int(request.GET.get('lenght'))
    thePassword=''
    for i in range(lenght):
        thePassword+=random.choice(characters)


    return render(request, 'generator/password.html', {'password':thePassword})

def info(request):
    return render(request, 'generator/info.html')