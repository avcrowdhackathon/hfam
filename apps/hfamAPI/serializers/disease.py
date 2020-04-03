from rest_framework import serializers

from apps.hfamAPI.models.disease import Disease


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = [
            "id",
            "socialDistancing",
            "annualAverage",
            "infectiousDays",
            "dateOfFirstHospitalizedCase",
            "hospitalization",
            "ventilationNeed",
            "icuNeed",
            "averageHospitalLengthOfStay",
            "averageDaysInICU",
            "averageDaysOnVentilator",
        ]
