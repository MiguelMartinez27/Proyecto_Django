from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Página por defecto "home"
    path("about/", views.about, name="about"),
    path("welcome/", views.welcome, name="welcome"),
    path("contact/", views.contact, name="contact"),
    path("contacto_exito/", views.contact_exito, name="contacto_exito"),
]
