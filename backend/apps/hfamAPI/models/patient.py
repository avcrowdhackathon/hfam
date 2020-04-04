from django.db import models

from .disease import Disease
from .hospital import Hospital

patientStates = [("DIAGNOSED", "Diagnosed"), ("HOSPITALIZED", "Hospitalized"), ("DISCHARGED", "Discharged")]
previousDiseases = [("RESPITATORY", "Respiratory"), ("HEART", "Heart"), ("INFLAMMATORY", "Inflammatory")]


class Patient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    state = models.CharField(max_length=15, choices=patientStates, default="DIAGNOSED")
    disease = models.ForeignKey(Disease, on_delete=models.SET_NULL, null=True, related_name="disease_of")
    previousDiseases = models.CharField(max_length=15, null=True, choices=previousDiseases)
    previousMedicine = models.TextField(null=True)
