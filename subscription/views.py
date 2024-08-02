from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
from .models import Subscription

def index(request):
    return render(request, 'base.html')

# Function that return the list of subscribtions
def subscriptions(request):
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        subscription.status = subscription.endDate > date.today()
    return render(request,'subscription/list.html', {'subscriptions': subscriptions})

# Function that add a new suscriber 
def addSubscription(request):
    if request.method == "POST": 
        surname = request.POST['surname']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']

        subscription = Subscription.objects.create(
            surname=surname,
            name=name,
            email=email,
            phone=phone,
            startDate=startDate,
            endDate=endDate
        )
        subscription.save()
        messages.success(request, "Abonnement ajouté avec succès")
        return redirect('subscriptions')
    
    return render(request, 'subscription/add.html')

# function that update subscription
def updateSubscription(request, id):
    subscription = Subscription.objects.get(id=id)
    if request.method == "POST":
        subscription.surname = request.POST['surname']
        subscription.name = request.POST['name']
        subscription.email = request.POST['email']
        subscription.phone = request.POST['phone']
        subscription.startDate = request.POST['startDate']
        subscription.endDate = request.POST['endDate']
        subscription.save()
        messages.success(request, "Abonnement modifié avec succès")
        return redirect('subscriptions')

    
    return render(request, 'subscription/update.html', {"subscription": subscription})

# function that update subscription
def reconductSubscription(request, id):
    subscription = Subscription.objects.get(id=id)
    if request.method == "POST":
        subscription.surname = request.POST['surname']
        subscription.name = request.POST['name']
        subscription.email = request.POST['email']
        subscription.phone = request.POST['phone']
        subscription.startDate = request.POST['startDate']
        subscription.endDate = request.POST['endDate']
        subscription.save()
        messages.success(request, "Reconduction effectué avec succès")
        return redirect('subscriptions')

    
    return render(request, 'subscription/reconduct.html', {"subscription": subscription})
