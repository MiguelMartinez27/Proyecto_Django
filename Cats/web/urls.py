from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),  # Página por defecto "home"
    path("about/", views.about, name="about"),
    path("welcome/", views.welcome, name="welcome"),
    path("contact/", views.contact, name="contact"),
    path("contacto_exito/", views.contact_exito, name="contacto_exito"),
    path("registro/", views.Registro.as_view(), name="registro"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
