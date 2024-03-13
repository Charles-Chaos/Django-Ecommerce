from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee


def index(request):
    demon =    Coffee.objects.all()
    return render(request, 'index.html', {'demon': demon})
