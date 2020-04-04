from rest_framework import serializers

from apps.hfamAPI.models.predictionInputs import PredictionInputs


class PredictionInputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionInputs
        fields = "__all__"
