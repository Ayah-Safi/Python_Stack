from django.shortcuts import render,redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        activity_dict = {}
        request.session['activities'] = activity_dict
    return render (request,'index.html')

def earn_gold(request):
    if request.method == 'POST':
        if request.POST['which_form'] == 'farm':
            earned_gold = random.randint(10, 20) 
            request.session['gold'] += earned_gold
            request.session['activities'][f"You entered a farm and earned {earned_gold} gold."] = 'green'

        elif request.POST['which_form'] == 'cave':
            earned_gold = random.randint(10, 20) 
            request.session['gold'] += earned_gold
            request.session['activities'][f"You entered a cave and earned {earned_gold} gold."] = 'green'
        
        elif request.POST['which_form'] == 'house':
            earned_gold = random.randint(10, 20) 
            request.session['gold'] += earned_gold
            request.session['activities'][f"You entered a house and earned {earned_gold} gold."] = 'green'
        
        else:
            earned_gold = random.randint(-50, 50) 
            request.session['gold'] += earned_gold
            if earned_gold > 0:
                request.session['activities'][f"You entered a quest and earned {earned_gold} gold."] = 'green'
            else:
                request.session['activities'][f"You failed a quest and lost {earned_gold} gold."] = 'red'

    print(request.session['activities'])
    return redirect('/')

def clear_session(request):
    if request.method == 'POST':
        if 'gold' in request.session:
            del request.session['gold']
        if 'activities' in request.session:
            del request.session['activities']
    return redirect('/')
    
    
        
        
        
        
    


