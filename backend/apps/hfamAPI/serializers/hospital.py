from rest_framework import serializers

from apps.hfamAPI.models.hospital import Hospital


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"
