from django.db import models

# Create your models here.

class Class(models.Model):
    CLASS_TERM_CHOICES = (
        ('F', 'Fall Only'),
        ('S', 'Spring Only'),
        ('FS', 'Fall/Spring'),
        ('FSS', 'Fall/Spring/Summer'),
    )
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    term = models.CharField(max_length=3,choices=CLASS_TERM_CHOICES,default='FS')
    credits = models.IntegerField()

class Requirement(models.Model):
    Class = models.ForeignKey(Class)
    PreReq = models.ForeignKey(Class)
    CoReq = models.ForeignKey(Class)

class Semester(models.Model):
    TERM_CHOICES = (
        ('F', 'Fall'),
        ('S', 'Spring'),
        ('SS', 'Summer'),
    )
    Year = models.IntegerField()
    Term = models.CharField(max_length=2, choices=TERM_CHOICES)

class SemClass(models.Model):
    Semester = models.ForeignKey(Semester)
    Class = models.ForeignKey(Class)

class DegreeSem(models.Model):


class DegreePlan(models.Model):
    Major = models.CharField(max_length=30)
    Type = models.CharField(max_length=6)
    Credits = models.IntegerField()
