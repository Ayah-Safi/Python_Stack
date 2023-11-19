from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return redirect ('/blogs')

def index(request):
    return HttpResponse ("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse ("placeholder to display a new form to create a new blog")

def create(request):
    return redirect ('/')

def show(request,number):
    return HttpResponse (f" placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse (f" placeholder to edit blog {number}")

def destroy(request,number):
        return redirect ('/')

def json(request):
        data = {
    'title': 'My First blog',
    'content': 'Lorem, ipsum dolor sit anet consectur adipiscing elit'
    }
        return JsonResponse(data)

