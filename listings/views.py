from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Titre
from listings.models import Listing


# listings/views.py

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
    'listings/band_list.html',  # pointe vers le nouveau nom de modèle
    {'bands': bands})
   
# listings/views.py


   
def band_detail(request, id):
    band = Band.objects.get(id=id) # notez le paramètre id supplémentaire
    return render(request,
        'listings/band_detail.html',
        {'band': band}) # nous passons l'id au modèle



# def hello(request):
#     bands = Band.objects.all()
#     return render(request, 'listings/hello.html',
#     {'bands': bands})
    

def apropos (request):
    return HttpResponse('essaie')

def about(request):
   return render(request, 'listings/about.html')

def services(request):
    titres = Listing.objects.all()
    return render(request, 'listings/titre.html',
    {'titres':titres})
    
   
def service_detail(request, id):
    titre = Listing.objects.get(id=id) # notez le paramètre id supplémentaire
    return render(request,
        'listings/service_detail.html',
        {'titre': titre}) # nous passons l'id au modèle

