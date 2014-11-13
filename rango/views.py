from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Rango says hey there world!')


def show(request):
    return render(request, 'rango/show.html', {'x': 'i am x'})
