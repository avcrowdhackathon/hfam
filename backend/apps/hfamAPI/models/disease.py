from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=50, unique=True)
    socialDistancing = models.FloatField()
    infectiousDays = models.IntegerField()
    dateOfFirstHospitalizedCase = models.DateField()
    hospitalization = models.FloatField()
    ventilationNeed = models.FloatField()
    icuNeed = models.FloatField()
    averageHospitalLengthOfStay = models.IntegerField()
    averageDaysInICU = models.IntegerField()
    averageDaysOnVentilator = models.IntegerField()
