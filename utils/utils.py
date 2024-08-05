from django.contrib import messages
from datetime import datetime

# fonction that clears the cache of messages
def clearMessage(request):
    if 'messages' in request.session:
        del request.session['messages']

# function that returns the current time
def currentTime():
    return datetime.now().time()
