from django import forms
from .models import *

class PredictionInputsForm(forms.Form):
  class Meta:
    model = PredictionInputs
    fields = "__all__"