from django.db import models

# Create your models here.


class ClassListing(models.Model):
    CLASS_TERM_CHOICES = (
        ('F', 'Fall Only'),
        ('S', 'Spring Only'),
        ('FS', 'Fall/Spring'),
        ('FSS', 'Fall/Spring/Summer'),
    )
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    term = models.CharField(max_length=3,choices=CLASS_TERM_CHOICES,default='FS')
    credits = models.IntegerField()


class Requirement(models.Model):
    Class = models.ForeignKey(ClassListing)
    PreReq = models.ForeignKey(ClassListing, related_name='Prereqs')
    CoReq = models.ForeignKey(ClassListing, related_name='Coreqs')


class Semester(models.Model):
    TERM_CHOICES = (
        ('F', 'Fall'),
        ('S', 'Spring'),
        ('SS', 'Summer'),
    )
    Number = models.IntegerField()
    Term = models.CharField(max_length=2, choices=TERM_CHOICES)


class SemClass(models.Model):
    Semester = models.ForeignKey(Semester)
    Class = models.ForeignKey(ClassListing)


class DegreePlan(models.Model):
    ENTRY_TERM_CHOICES = (
        ('F', 'Fall'),
        ('S', 'Spring'),
    )
    Major = models.CharField(max_length=30, primary_key=True)
    Credits = models.IntegerField()
    Entry = models.CharField(max_length=1, choices=ENTRY_TERM_CHOICES, default='F"')


class DegreeSem(models.Model):
    Degree = models.ForeignKey(DegreePlan)
    Semester = models.ForeignKey(Semester)
