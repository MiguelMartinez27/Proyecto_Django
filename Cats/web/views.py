from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Rascadores
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/contacto_exito/")
    else:
        form = ContactForm()
    return render(request, "web/contact.html", {"form": form})


def contact_exito(request):
    return render(request, "web/contacto_exito.html")


def home(request):
    rascadores_publicos = Rascadores.objects.filter(is_private=False)
    return render(request, "web/home.html", {"rascadores": rascadores_publicos})


@login_required
def welcome(request):
    rascadores_privados = Rascadores.objects.filter(is_private=True)
    return render(request, "web/welcome.html", {"rascadores": rascadores_privados})


def about(request):
    return render(request, "web/about.html")


class Registro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # Redirige al login después del registro
    template_name = "registration/registro.html"


class LogoutView(generic.CreateView):
    next_page = "/home/"
    template_name = "registration/logout.html"
