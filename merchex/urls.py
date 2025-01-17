"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #les chemin pour les bands
    path('bands/',views.band_list,name='band-list'),
    path('bands/<int:id>/', views.band_detail,name='band-detail'), # ajouter ce motif sous notre autre motif de groupes
    path('bands/add/', views.band_create, name='band-create'),
    path('email-sent/',views.email_sent,name='email-sent'),
    path('bands/<int:id>/change/', views.band_change,name='band-change'), # ajouter ce motif sous notre autre motif de groupes
    path('bands/<int:id>/delete/', views.band_delete,name='band-delete'), # ajouter ce motif sous notre autre motif de groupes
    
    
    
    path('about-us/',views.about,name='about-us'),
    path('contact-us/',views.contact,name='contact'),
    
    path('services/',views.services,name='service-list'),
    path('services/<int:id>/',views.service_detail,name='service-detail'),
    path('services/add/',views.services_create,name='service-create'),
    path('services/<int:id>/change/', views.service_change,name='service-change'), 
    path('services/<int:id>/delete/', views.service_delete,name='service-delete'), 
    
    
    
]
