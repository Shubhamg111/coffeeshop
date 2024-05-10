from django.urls import path
from .  import views


urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('aboutpage',views.aboutpage, name='aboutpage'),
    path('servicepage',views.servicepage, name='servicepage'),
    path('reservationpage',views.reservationpage, name='reservationpage'),
    path('testimonialspage',views.testimonialspage, name='testimonialspage'),
    path('contactpage',views.contactpage, name='contactpage'),
    path('menupage',views.menupage, name='menupage'),



]
