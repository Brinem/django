from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contactus.html')


def gallery(request):
    return render(request, 'gallery.html')
