from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'application.html')


def plan(request):
    return render(request, 'plan.html')


def importScreen(request):
    return render(request, 'import.html')


def options(request):
    return render(request, 'options.html')