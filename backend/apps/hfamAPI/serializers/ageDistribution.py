from rest_framework import serializers

from apps.hfamAPI.models.ageDistribution import AgeDistribution


class AgeDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeDistribution
        fields = ["id", "ages0_25", "ages26_50", "ages51_75", "ages76_100"]
