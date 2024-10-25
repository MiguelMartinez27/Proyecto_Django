from django.shortcuts import render
from .models import Rascadores


def home(request):
    rascadores_publicos = Rascadores.objects.filter(is_private=False)
    return render(request, "web/home.html", {"rascadores": rascadores_publicos})


def welcome(request):
    rascadores_pivados = Rascadores.objects.filter(is_private=True)
    return render(request, "web/welcome.html", {"rascadores": rascadores_pivados})


def about(request):
    return render(request, "web/about.html")
