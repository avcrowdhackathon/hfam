from rest_framework import serializers

from apps.hfamAPI.models.doctor import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "specialty", "hospital", "timetable"]
