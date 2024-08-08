from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Session, Package
from datetime import datetime
from utils.utils import clearMessage, currentTime

# Create your views here.
def sessions(request):
    # loading sessions and status process 
    sessions = Session.objects.all()
    for session in sessions:
        session.status = session.date < datetime.now().date()

    return render(request, 'session/list.html', {'sessions': sessions})



# Function that add a new suscriber 
def addSession(request):
    clearMessage(request)
    # loading variables to pass to template
    packages = Package.objects.all()

    # check if adding requested then process
    if request.method == "POST": 
        surname = request.POST['surname']
        name = request.POST['name']
        phone = request.POST['phone']
        package = request.POST['package']

        # load the package with given id
        addPackage = Package.objects.get(id=package)
        

        subscription = Session.objects.create(
            surname=surname,
            name=name,
            phone=phone,
            package=addPackage
        )
        subscription.save()
        clearMessage(request)
        messages.success(request, "Séance ajouté avec succès")
        return redirect('sessions')
    
    return render(request, 'session/add.html', {'packages': packages})

def updateSession(request):
    clearMessage(request)
    # loading variables to pass to templates
    packages = Package.objects.all()
    id = request.POST.get('id')
    session = Session.objects.get(id=id)
    today = datetime.now().date()
    # check if reconduction requested if yes reconduct 
    updateStatus = request.POST.get('updateStatus')
    if updateStatus:
        session.surname = request.POST['surname']
        session.name = request.POST['name']
        session.phone = request.POST['phone']
        session.date = request.POST['date']
        session.hour = request.POST['hour']
        package = request.POST['package']

        # load the package with given id
        updatedPackage = Package.objects.get(id=package)
      
        session.package = updatedPackage
        session.save()
        messages.success(request, "séance modifié avec succès")
        return redirect('sessions')
    
    context = {
        "session": session,
        "packages": packages,
        "max_date": today
    }

    return render(request, 'session/update.html', context)

    
# function that update subscription
def reconductSession(request):
    clearMessage(request)
    # loading variables to pass the templates
    packages = Package.objects.all()
    id = request.POST.get('id')
    session = Session.objects.get(id=id)

    # check if reconduction requested if yes reconduct 
    updateStatus = request.POST.get('updateStatus')
    if updateStatus:
        surname = request.POST['surname']
        name = request.POST['name']
        phone = request.POST['phone']
        package = request.POST['package']

        # load the package with given id
        addPackage = Package.objects.get(id=package)
        
        session = Session.objects.create(
            surname=surname,
            name=name,
            phone=phone,
            package=addPackage
        )
        session.save()
        clearMessage(request)
        messages.success(request, "Séance ajouté avec succès")
        return redirect('sessions')

    context = {
        "session": session,
        "packages": packages
    }

    
    return render(request, 'session/reconduct.html', context)

    # function that deleter a subscription
def deleteSession(request):
    clearMessage(request) 
    
    # load the session
    id = request.POST.get('id')
    session = Session.objects.get(id=id)

    # check if deletion requested if yes delete and return to session's List
    updateStatus = request.POST.get('updateStatus')
    if updateStatus:
        session.delete()
        messages.success(request, "Séance supprimé avec succès.")
        return redirect('sessions')
    
    return render(request, 'session/delete.html', {"session": session})
