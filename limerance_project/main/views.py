
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



def services(request):
    return render(request, 'service.html')

def other_services(request):
    return render(request, 'other_services.html')