from django.shortcuts import render,redirect
from users_app.models import User

def index(request):
    data = User.objects.all()
    context = {'users': data}
    return render(request, 'index.html', context)

def form(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        User.objects.create(first_name = first_name,last_name  = last_name,email = email, age = age)
    return redirect('/')