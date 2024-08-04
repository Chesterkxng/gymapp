from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from .models import Subscription, Package
from utils.utils import clearMessage

def index(request):
    clearMessage(request)
    return render(request, 'base.html')

# Function that return the list of subscribtions
def subscriptions(request):
    clearMessage(request)
    # variables to pass to templates
    subscriptions = Subscription.objects.all()
  
    for subscription in subscriptions:
        subscription.status = subscription.endDate > date.today()
    return render(request,'subscription/list.html', {'subscriptions': subscriptions})

# Function that add a new suscriber 
def addSubscription(request):
    clearMessage(request)
    # variables to pass to templates
    packages = Package.objects.all()

    if request.method == "POST": 
        surname = request.POST['surname']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        startDate = request.POST['startDate']
        duration = request.POST['duration']
        package = request.POST['package']

        # load the package with given id
        addPackage = Package.objects.get(id=package)
        # computing the subscription ending date based on requested duration
        start_date = datetime.strptime(startDate, '%Y-%m-%d').date()
        endDate = start_date + relativedelta(months=int(duration))

        subscription = Subscription.objects.create(
            surname=surname,
            name=name,
            email=email,
            phone=phone,
            startDate=startDate,
            duration=duration,
            endDate=endDate,
            package=addPackage
        )
        subscription.save()
        clearMessage(request)
        messages.success(request, "Abonnement ajouté avec succès")
        return redirect('subscriptions')
    
    return render(request, 'subscription/add.html', {'packages': packages})

# function that update subscription
def updateSubscription(request):
    clearMessage(request)
    # variables to pass to templates
    packages = Package.objects.all()
    id = request.POST.get('id')
    subscription = Subscription.objects.get(id=id)

    updateStatus = request.POST.get('updateStatus')
    if updateStatus:
        subscription.surname = request.POST['surname']
        subscription.name = request.POST['name']
        subscription.email = request.POST['email']
        subscription.phone = request.POST['phone']
        subscription.startDate = request.POST['startDate']
        subscription.duration = request.POST['duration']
        package = request.POST['package']

        # load the package with given id
        updatedPackage = Package.objects.get(id=package)
        # computing the subscription ending date based on requested duration
        start_date = datetime.strptime(request.POST['startDate'], '%Y-%m-%d').date()
        endDate = start_date + relativedelta(months=int(request.POST['duration']))
        subscription.endDate = endDate
        subscription.package = updatedPackage
        subscription.save()
        messages.success(request, "Abonnement modifié avec succès")
        return redirect('subscriptions')

    
    return render(request, 'subscription/update.html', {"subscription": subscription, "packages": packages})

# function that update subscription
def reconductSubscription(request):
    clearMessage(request)
    # variables to pass to template
    packages = Package.objects.all()
    id = request.POST.get('id')
    subscription = Subscription.objects.get(id=id)

    updateStatus = request.POST.get('updateStatus')
    if updateStatus:
        surname = request.POST['surname']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        startDate = request.POST['startDate']
        duration = request.POST['duration']
        package = request.POST['package']

        # load the package with given id
        addPackage = Package.objects.get(id=package)
        # computing the subscription ending date based on requested duration
        start_date = datetime.strptime(startDate, '%Y-%m-%d').date()
        endDate = start_date + relativedelta(months=int(duration))

        subscription = Subscription.objects.create(
            surname=surname,
            name=name,
            email=email,
            phone=phone,
            startDate=startDate,
            duration=duration,
            endDate=endDate,
            package=addPackage
        )
        subscription.save()
        messages.success(request, "Reconduction effectué avec succès")
        return redirect('subscriptions')

    
    return render(request, 'subscription/reconduct.html', {"subscription": subscription, "packages": packages})

# function that deleter a subscription
def deleteSubscription(request):
    id = request.POST.get('id')
    subscription = Subscription.objects.get(id=id)
    updateStatus = request.POST.get('updateStatus')
    if updateStatus:
        subscription.delete()
        messages.success(request, "Abonnement supprimé avec succès.")
        return redirect('subscriptions')
    
    return render(request, 'subscription/delete.html', {"subscription": subscription})

