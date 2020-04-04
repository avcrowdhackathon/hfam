from rest_framework import serializers

from apps.hfamAPI.models.predictionOutputs import PredictionOutputs


class PredictionOutputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionOutputs
        fields = "__all__"
