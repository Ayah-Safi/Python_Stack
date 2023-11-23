from django.shortcuts import render,redirect
import random
from datetime import datetime

def index(request):
    request.session['gold'] = 0
    return render (request,'index.html')

def earn_gold(request):
    if request.method == 'POST':
        your_gold = 0
        activities = []

        if 'gold' in request.session:
            your_gold = request.session['gold']
            if 'activities' in request.session:
                activities = request.session['activities']

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if request.POST['which_form'] == 'farm':
            earned_gold = round((random.random() * 10) + 10)
            your_gold += earned_gold
            activities.append({'activity':f"You entered a farm and earned {earned_gold} gold.",'time':time})

        elif request.POST['which_form'] == 'cave':
            earned_gold = round((random.random() * 10) + 10)
            your_gold += earned_gold
            activities.append({'activity':f"You entered a cave and earned {earned_gold} gold.",'time':time})

        elif request.POST['which_form'] == 'house':
            earned_gold = round((random.random() * 10) + 10)
            your_gold += earned_gold
            activities.append({'activity':f"You entered a house and earned {earned_gold} gold.",'time':time})
        else:
            earned_gold = round((random.random() * 10) + 40)
            your_gold += earned_gold
            activities.append({'activity':f"You completed a quest and earned {earned_gold} gold.",'time':time})

        request.session['gold'] = your_gold
        request.session['activities'] = activities

        data = {'gold': your_gold, 'activities': activities}
        return render(request, 'index.html', data)
            
    
    
        
        
        
        
    


