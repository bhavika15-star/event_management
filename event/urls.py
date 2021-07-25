from django.contrib import admin
from django.urls import path,include
from event import views

urlpatterns = [
    path('',views.event,name='home'),
    path('about',views.about,name='about'),
    path('payment',views.payment,name='payment'),
    path('contact',views.contact,name='contact-us'),
    path('services',views.services,name='service'),
    path('bday',views.bday,name='birth-day'),
    path('wedding',views.wedding,name='wedding'),
    path('concert',views.concert,name='concert'),
    path('thanks',views.thanks,name='thanks'),
]