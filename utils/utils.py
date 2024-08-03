from django.contrib import messages

def clearMessage(request):
    if 'messages' in request.session:
        del request.session['messages']