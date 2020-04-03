from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hfamAPI.models.disease import Disease
from apps.hfamAPI.serializers.disease import DiseaseSerializer


# /diseases
class DiseaseList(APIView):
    """
    List all Diseases, or create a new Disease.
    """

    def get(self, request):
        diseases = Disease.objects.all()
        serializer = DiseaseSerializer(diseases, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Creates an Age Distribution", request_body=DiseaseSerializer)
    def post(self, request):
        serializer = DiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# /diseases/{id}
class DiseaseDetail(APIView):
    """
    Retrieve, update or delete a Disease instance.
    """

    def get_object(self, pk):
        try:
            return Disease.objects.get(pk=pk)
        except Disease.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        disease = self.get_object(pk)
        serializer = DiseaseSerializer(disease)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        disease = self.get_object(pk)
        serializer = DiseaseSerializer(disease, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        disease = self.get_object(pk)
        disease.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
