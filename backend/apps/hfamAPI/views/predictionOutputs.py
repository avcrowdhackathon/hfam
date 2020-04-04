from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hfamAPI.models.predictionOutputs import PredictionOutputs
from apps.hfamAPI.serializers.predictionOutputs import PredictionOutputsSerializer


# /predictionOutputs
class PredictionOutputsList(APIView):
    """
    List all PredictionOutputs, or create a new PredictionOutputs.
    """

    def get(self, request):
        prediction_inputs = PredictionOutputs.objects.all()
        serializer = PredictionOutputsSerializer(prediction_inputs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Creates an Prediction Output", request_body=PredictionOutputsSerializer)
    def post(self, request):
        serializer_inputs = PredictionOutputsSerializer(data=request.data)
        # Maps the POST data fields to the fields used in the simulation for easier flattening
        if serializer_inputs.is_valid():
            serializer_inputs.save()
            return Response(serializer_inputs.data, status=status.HTTP_201_CREATED)
        return Response(serializer_inputs.errors, status=status.HTTP_400_BAD_REQUEST)


# /predictionOutputs/{id}
class PredictionOutputsDetail(APIView):
    """
    Retrieve, update or delete a PredictionOutputs instance.
    """

    def get_object(self, pk):
        try:
            return PredictionOutputs.objects.get(pk=pk)
        except PredictionOutputs.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        prediction_input = self.get_object(pk)
        serializer = PredictionOutputsSerializer(prediction_input)
        return Response(serializer.data)

    def put(self, request, pk):
        prediction_input = self.get_object(pk)
        serializer = PredictionOutputsSerializer(prediction_input, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prediction_input = self.get_object(pk)
        prediction_input.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
