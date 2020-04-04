from django.db import models
from jsonfield import JSONField

from .predictionInputs import PredictionInputs


class PredictionOutputs(models.Model):
    dateTime = models.DateTimeField(auto_now_add=True)
    predictionInputs = models.OneToOneField(PredictionInputs, on_delete=models.CASCADE,
                                            related_name="prediction_inputs_of")
    admittedPatients = JSONField()
    census = JSONField()
    sir = JSONField()
    test = models.IntegerField(null=True)
