from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/new')
    else:
        created_object = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        date = request.POST['date'],
        desc = request.POST['desc'],)
        id = created_object.id
        messages.success(request, "TV show successfully created")
        return redirect(f'/shows/{id}')

def showTV(request, id):
    x = Show.objects.get(id=id)
    context = {
        'id' : x.id,
        'title' : x.title,
        'network' : x.network,
        'date' : x.date,
        'desc' : x.desc,
        'updated_at' : x.updated_at
    }
    return render(request, 'showTV.html', context)

def shows(request):
    all_shows = Show.objects.all()
    context={
        'all_shows' : all_shows
    }
    return render(request, 'shows.html', context)

def edit_show(request, id):
    y = Show.objects.get(id=id)    
    context = {
        "show": y
    }
    return render(request, 'edit.html', context)

def update_show(request):
    errors = Show.objects.basic_validator(request.POST)
    id = request.POST['id']
    k = Show.objects.get(id= request.POST['id'])
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'{id}/edit')
    else:
        k.title = request.POST['title']
        k.network = request.POST['network']
        k.date = request.POST['date']
        k.desc = request.POST['desc']
        k.save()
        return redirect(f'/shows/{k.id}')

def delete_show(request, id):
    d = Show.objects.get(id=id)
    d.delete()
    return redirect('/shows')

