from django.db import models


class Inventory(models.Model):
    masks = models.IntegerField()
    gloves = models.IntegerField()
    ventilators = models.IntegerField()
