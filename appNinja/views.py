from django.shortcuts import render, HttpResponse, redirect
import random
import time

def index(request):
    return render(request, 'appNinja/index.html')


def monedas(request):
    if 'logs' not in request.session:
            request.session['logs'] =[]
    if 'contador' in request.session:
        if request.POST['ninja'] == 'granja':
            farm = random.randint(0,10)
            print(farm)
            request.session['contador'] += farm
            datos= {
            'texto': f" Ganaste: {farm } monedas en la Granja -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" ,
             'color': 'verde' if (farm >= 0)  else 'rojo' ,
            }
            request.session['logs'].append(datos)
            request.session.save()
            
        if request.POST['ninja'] == 'cueva':
            cave= random.randint(5,10)
            request.session['contador'] += cave
            datos= {
            'texto': f" Ganaste: {cave } monedas en la Cueva -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" ,
             'color': 'verde' if (cave >= 0)  else 'rojo' ,
            }
            request.session['logs'].append(datos)
            request.session.save()
            print(request.session['contador'])
        if request.POST['ninja'] == 'casa':
            house=random.randint(2,5)
            request.session['contador'] += house
            datos= {
            'texto': f" Ganaste: {house } monedas en la Casa -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" ,
             'color': 'verde' if (house >= 0)  else 'rojo' ,
            }
            request.session['logs'].append(datos)
            request.session.save()
            print(request.session['contador'])
        if request.POST['ninja'] == 'casino':
            casino= random.randint(-50,50)
            request.session['contador'] += casino
            datos= {
            'texto': 'Ganaste: ' f"{casino} monedas en el Casino -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" if (casino >= 0)  else 'Perdiste: ' f"{casino} monedas en el Casino -- {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}" ,
            'color': 'verde' if (casino >= 0)  else 'rojo' ,
            }
            request.session['logs'].append(datos)
            request.session.save()
            print(request.session['contador'])
        

    else:
        request.session['contador'] = 0
        
    return redirect("/")

def resetear(request):
    if 'contador' in request.session:
        del request.session['contador']
    if 'logs' in request.session:
        del request.session['logs']
    return redirect("/")


