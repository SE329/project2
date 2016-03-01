from django.contrib import admin
from .models import *

# Register your models here.

#admin.site.register(DegreePlan)
#admin.site.register(Semester)
#admin.site.register(ClassListing)
#admin.site.register(Requirement)


@admin.register(DegreePlan)
class DegreePlanAdmin(admin.ModelAdmin):
    list_display = ['Major']


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['Number', 'Term', 'Classes']
