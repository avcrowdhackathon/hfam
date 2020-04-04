from django.db import models

from .inventory import Inventory
from .region import Region


class Hospital(models.Model):
    name = models.CharField(max_length=50, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, related_name="inventory_of")
    marketShare = models.FloatField()
    currentHospitalized = models.IntegerField()
    capacity = models.IntegerField()
