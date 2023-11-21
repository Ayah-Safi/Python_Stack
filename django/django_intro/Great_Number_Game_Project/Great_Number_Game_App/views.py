from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):   
    request.session['random_number'] = random.random() * 100
    if request.method == 'POST':
        request.session['number'] = int(request.POST['number'])
        return redirect('/result')
    return render(request, 'index.html')

def result(request):
    if request.session['random_number'] ==  request.session['number']:
        return render (request, 'result2.html', {'ans': "was the number"})
    elif request.session['random_number'] > request.session['number']:
        return render (request, 'result.html',{'ans': "Too low!"})
    else:
        return render (request, 'result.html', {'ans': "Too high!"})