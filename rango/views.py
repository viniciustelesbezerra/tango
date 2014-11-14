from django.shortcuts import render


def index(request):
    return render(request, 'rango/index.html')


def show(request):
    return render(request, 'rango/show.html', {'x': 'i am x'})
