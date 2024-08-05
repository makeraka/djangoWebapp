from django.contrib import admin

# Register your models here.
from listings.models import Band
from listings.models import Listing

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste
    
class ListingAdmin(admin.ModelAdmin) :
    list_display = ('titre','description','sold', 'year','type','band')
    

admin.site.register(Band,BandAdmin)
admin.site.register(Listing,ListingAdmin)
