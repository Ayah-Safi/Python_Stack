from django.shortcuts import render,redirect
from dojo_and_ninja_shell_app.models import *
all_dojos = Dojos.objects.all()

def index(request):
    dojo_dict = {}
    all_dojos = Dojos.objects.all()
    dojo_dict['dojos'] = all_dojos
    return render(request, 'index.html',dojo_dict)

def processDojo(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
    Dojos.objects.create(name = name, city = city, state=state )
    return redirect('/')

def processNinja(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dojo = request.POST['dojo']
        dojo_object = Dojos.objects.get(id=dojo)
    Ninjas.objects.create(first_name = first_name, last_name = last_name, dojos = dojo_object )
    return redirect('/')
    