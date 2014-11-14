from django.shortcuts import render
from rango.models import Category


def index(request):
    return render(request, 'rango/index.html',
                  {'categories': Category.objects.order_by('-likes')[:5]})


def show(request):
    return render(request, 'rango/show.html', {'x': 'i am x'})
