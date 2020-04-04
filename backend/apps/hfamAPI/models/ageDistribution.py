from django.db import models


class AgeDistribution(models.Model):
    ages0_25 = models.FloatField()
    ages26_50 = models.FloatField()
    ages51_75 = models.FloatField()
    ages76_100 = models.FloatField()
