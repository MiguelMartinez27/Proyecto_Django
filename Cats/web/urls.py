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
    # views rascadores
    path("rascadores/", views.RascadoresListView.as_view(), name="rascadores_list"),
    path(
        "rascadores/<uuid:pk>/",
        views.RascadoresDetailView.as_view(),
        name="rascadores_detail",
    ),
    path(
        "rascadores/nuevo/",
        views.RascadoresCreateView.as_view(),
        name="rascadores_create",
    ),
    path(
        "rascadores/<uuid:pk>/editar/",
        views.RascadoresUpdateView.as_view(),
        name="rascadores_update",
    ),
    path(
        "rascadores/<uuid:pk>/eliminar/",
        views.RascadoresDeleteView.as_view(),
        name="rascadores_delete",
    ),
]
