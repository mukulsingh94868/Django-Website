from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(requests):
    context = {
        'variable': "this is sent"
    }
    
    return render(requests, 'index.html', context)

def about(requests):
    #return HttpResponse("this is aboutpage")
    return render(requests, 'about.html')    

def services(requests):
    #return HttpResponse("this is servicespage")
    return render(requests, 'services.html')
     
     

def contact(request):
    #return HttpResponse("this is contactpage") 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')

        contact = Contact(name=name, email=email, phone=phone, city=city)
        contact.save()
        messages.success(request, 'Your Response has been Saved!')
    return render(request, 'contact.html')    