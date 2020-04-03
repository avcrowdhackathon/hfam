from rest_framework import serializers

from apps.hfamAPI.models.region import Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name", "population", "boundaries", "ageDistribution"]
