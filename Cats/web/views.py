from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Rascadores
from .forms import ContactForm


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


def welcome(request):
    rascadores_pivados = Rascadores.objects.filter(is_private=True)
    return render(request, "web/welcome.html", {"rascadores": rascadores_pivados})


def about(request):
    return render(request, "web/about.html")
