from django.db import models


class PredictionInputs(models.Model):
    population = models.IntegerField()
    hospitalMarketShare = models.FloatField()
    currentHospitalized = models.IntegerField()
    dateOfFirstHospitalizedCase = models.DateField()
    socialDistancing = models.FloatField()
    hospitalizationPercent = models.FloatField()
    icuNeedPercent = models.FloatField()
    ventilationNeedPercent = models.FloatField()
    infectiousDays = models.IntegerField()
    averageHospitalLengthOfStay = models.IntegerField()
    averageDaysInICU = models.IntegerField()
    averageDaysOnVentilator = models.IntegerField()
    numberOfDaysToProject = models.IntegerField()
