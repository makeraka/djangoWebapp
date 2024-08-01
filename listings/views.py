from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Titre



def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',
    {'bands': bands})
    

def apropos (request):
    return HttpResponse('essaie')

def about(request):
   return render(request, 'listings/about.html')

def services(request):
    titres = Titre.objects.all()
    return render(request, 'listings/titre.html',
    {'titres':titres})
