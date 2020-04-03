from django.db import models

from .ageDistribution import AgeDistribution


class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)
    population = models.IntegerField()
    boundaries = models.CharField(max_length=200)
    ageDistribution = models.OneToOneField(AgeDistribution, on_delete=models.CASCADE,
                                           related_name="age_distribution_of")

    class Meta:
        ordering = ["name"]
