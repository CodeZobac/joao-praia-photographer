from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def photos(request):
    return render(request, "photos.html")


def shop(request):
    return render(request, "shop.html")
