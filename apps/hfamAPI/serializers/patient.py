from rest_framework import serializers

from apps.hfamAPI.models.patient import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "hospital", "state", "disease"]
