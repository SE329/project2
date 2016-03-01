from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    return render(request, 'application.html')


def plan(request):
    requestedplan = 'Software Engineering'
    useplan = DegreePlan.objects.get(Major=requestedplan)
    plans = DegreePlan.objects.all()
    classes = ClassListing.objects.all()
    semesters = [useplan.Semester1, useplan.Semester2, useplan.Semester3, useplan.Semester4, useplan.Semester5,
                 useplan.Semester6, useplan.Semester7, useplan.Semester8]
    classlist = []
    semCredits = []

    for s in semesters:
        semlist = s.Classes.split(';')
        semesterlist = []
        scredits = 0
        for item in semlist:
            if len(item) > 0:
                thisclass = ClassListing.objects.get(code=item)
                scredits += thisclass.credits
                semesterlist.append(thisclass)
        classlist.append(semesterlist)
        semCredits.append(scredits)

    context = {
        'allplans': plans,
        'allclasses': classes,
        'plan' : requestedplan,
        'credits' : useplan.Credits,
        'classList': classlist,
        'semCredits': semCredits
    }

    return render(request, 'plan.html', context)


def importScreen(request):
    return render(request, 'import.html')


def options(request):
    useplan = DegreePlan.objects.all()
    context = {
        'plans': useplan
    }
    return render(request, 'options.html', context)

