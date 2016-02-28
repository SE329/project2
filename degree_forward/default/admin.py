from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(DegreePlan)
admin.site.register(Semester)
admin.site.register(ClassListing)

admin.site.register(Requirement)
admin.site.register(DegreeSem)
admin.site.register(SemClass)