from django.shortcuts import render


def home(request):
    return render(request, "web/home.html")


def welcome(request):
    return render(request, "web/welcome.html")


def about(request):
    return render(request, "web/about.html")
