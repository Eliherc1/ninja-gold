from django.shortcuts import render, HttpResponse, redirect
import random
import time

def index(request):
    return render(request, 'appNinja/index.html')


def monedas(request):
    if 'contador' in request.session:
        if request.POST['ninja'] == 'granja':
            monedas = random.randint(0,10)
            request.session['contador'] += monedas
        if request.POST['ninja'] == 'cueva':
            monedas= random.randint(5,10)
            request.session['contador'] += monedas
        if request.POST['ninja'] == 'casa':
            monedas=random.randint(2,5)
            request.session['contador'] += monedas
        if request.POST['ninja'] == 'casino':
            monedas= random.randint(-50,50)
            request.session['contador'] += monedas

    else:
        request.session['contador'] = 0
        
    return redirect("/")

def resetear(request):
    request.session['contador'] = 0 
    return redirect("/")


