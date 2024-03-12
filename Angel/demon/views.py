from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee


def home(request):
    demon =    Coffee.objects.all()
    return render(request, 'home.html', {'demon': demon})