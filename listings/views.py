from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Titre
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm, ContactUsForm,ListingForm


# listings/views.py

#vue pour la liste des bandes
def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
    'listings/band_list.html',  # pointe vers le nouveau nom de modèle
    {'bands': bands})
   


#vue pour detail band
def band_detail(request, id):
    band = Band.objects.get(id=id) # notez le paramètre id supplémentaire
    return render(request,
        'listings/band_detail.html',
        {'band': band}) # nous passons l'id au modèle

#vue pour ajouter une bande
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()
    return render(request, 
            'listings/band_create.html',
            {'form': form})



#vue pour changer ou modifier une  bande
def band_change(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_change.html',
                {'form': form})
    



#supprimer un groupe
def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})


def email_sent(request):
    return render(request, 'listings/email_sent.html')
    
#vue pour apropos
def about(request):
   return render(request, 'listings/about.html')

#vue pour Listing
def services(request):
    titres = Listing.objects.all()
    return render(request, 'listings/titre.html',
    {'titres':titres})
    
    
 #vue pour detail listing  
def service_detail(request, id):
    titre = Listing.objects.get(id=id) # notez le paramètre id supplémentaire
    return render(request,
        'listings/service_detail.html',
        {'titre': titre}) # nous passons l'id au modèle
    
    
    
    
#vue pour ajouter une bande
def services_create(request):
    if request.method == 'POST':
        form =ListingForm (request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('service-detail', band.id)

    else:
        form = ListingForm()
    return render(request, 
            'listings/services_create.html',
            {'form': form})


#vue pour changer ou modifier une  liste
def service_change(request, id):
    list = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=list)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('service-detail', list.id)
    else:
        form = ListingForm(instance=list)

    return render(request,
                'listings/service_change.html',
                {'form': form})


#supprimer une liste
def service_delete(request, id):
    list = Listing.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        list.delete()
        # rediriger vers la liste des groupes
        return redirect('service-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/service_delete.html',
                    {'list': list})

    
    
    

#vue pour verifier les contactes entrez au formulaire :
def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST) # ajout d’un nouveau formulaire ici
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            return redirect('email-sent')  # ajoutez cette instruction de retour
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        form = ContactUsForm()
    return render(request,
        'listings/contact.html',
        {'form': form})  # passe ce formulaire au gabarit