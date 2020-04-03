from django.db import models

from .hospital import Hospital
from .timetable import TimeTable


class Doctor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    specialty = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True)
    timetable = models.OneToOneField(TimeTable, on_delete=models.CASCADE, related_name="timetable_of")
