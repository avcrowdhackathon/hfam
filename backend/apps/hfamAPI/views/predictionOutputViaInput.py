from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.hfamAPI.models.predictionOutputs import PredictionOutputs
from apps.hfamAPI.serializers.predictionOutputs import PredictionOutputsSerializer


@api_view(['GET'])
def get_prediction_output_via_input(request, p_inputs_k):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        prediction_output = PredictionOutputs.objects.get(predictionInputs=p_inputs_k)
    except PredictionOutputs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PredictionOutputsSerializer(prediction_output)
        return Response(serializer.data)