from django.db import models

# Create your models here.
# listings/models.py

from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    
    #imbrication : definir la classe genre dans Band pour permetre d'avoir une liste deroulante.
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    like_new = models.fields.BooleanField(default=False)
   
    #methode permettant d'afficher le nom de nos bands :
    def __str__(self):
        return f'{self.name}'
    
    
class Titre(models.Model):
    titre = models.fields.CharField(max_length=100) 
    
class Listing (models.Model):
    
    class Type(models.TextChoices):
        disques = 'Records'
        vêtements = 'Clothing'
        affiches = 'Posters'
        divers = 'Miscellaneous'
        
    titre = models.fields.CharField(max_length=100) 
    description = models.fields.CharField(max_length=100) 
    sold = models.fields.IntegerField()
    year = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    type=models.fields.CharField(choices=Type.choices, max_length=30)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.titre}'
    
    
    
