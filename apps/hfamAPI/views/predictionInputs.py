import datetime

from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hfamAPI.models.predictionInputs import PredictionInputs
from apps.hfamAPI.serializers.predictionInputs import PredictionInputsSerializer
from apps.hfamAPI.views.predictionOutputs import PredictionOutputsList
from apps.simulation.models import SimSirModel
from apps.simulation.parameters import construct_parameters


# /predictionInputs
class PredictionInputsList(APIView):
    """
    List all PredictionInputs, or create a new PredictionInputs.
    """

    def get(self, request):
        prediction_inputs = PredictionInputs.objects.all()
        serializer = PredictionInputsSerializer(prediction_inputs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Creates an Age Distribution", request_body=PredictionInputsSerializer)
    def post(self, request):
        request_data = request.data
        serializer_inputs = PredictionInputsSerializer(data=request_data)
        # Maps the POST data fields to the fields used in the simulation for easier flattening
        if serializer_inputs.is_valid():
            # Here we save the prediction inputs to the DB
            serializer_inputs.save()
            # After saving we want to construct the parameters and initiate the simulation
            parameters = construct_parameters(request_data)
            outputs = SimSirModel(parameters)
            prediction_output_view = PredictionOutputsList()
            # After simulation is complete we want to save the simulation outputs to the DB
            prediction_output_view.post({
                "dateTime": datetime.datetime.now(), "predictionInputs": request_data.get("id", 1),
                "admittedPatients": outputs.admits_df.to_json(), "census": outputs.census_df.to_json(),
                "sir": outputs.sim_sir_w_date_df.to_json()
            })
            return Response(serializer_inputs.data, status=status.HTTP_201_CREATED)
        return Response(serializer_inputs.errors, status=status.HTTP_400_BAD_REQUEST)


# /predictionInputs/{id}
class PredictionInputsDetail(APIView):
    """
    Retrieve, update or delete a PredictionInputs instance.
    """

    def get_object(self, pk):
        try:
            return PredictionInputs.objects.get(pk=pk)
        except PredictionInputs.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        prediction_input = self.get_object(pk)
        serializer = PredictionInputsSerializer(prediction_input)
        return Response(serializer.data)

    def put(self, request, pk):
        prediction_input = self.get_object(pk)
        serializer = PredictionInputsSerializer(prediction_input, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prediction_input = self.get_object(pk)
        prediction_input.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
