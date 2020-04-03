from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hfamAPI.models.ageDistribution import AgeDistribution
from apps.hfamAPI.serializers.ageDistribution import AgeDistributionSerializer


# /ageDistributions
class AgeDistributionList(APIView):
    """
    List all AgeDistributions, or create a new AgeDistribution.
    """

    def get(self, request):
        ageDistributions = AgeDistribution.objects.all()
        serializer = AgeDistributionSerializer(ageDistributions, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Creates an Age Distribution", request_body=AgeDistributionSerializer)
    def post(self, request):
        serializer = AgeDistributionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# /ageDistributions/{id}
class AgeDistributionDetail(APIView):
    """
    Retrieve, update or delete a AgeDistribution instance.
    """

    def get_object(self, pk):
        try:
            return AgeDistribution.objects.get(pk=pk)
        except AgeDistribution.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ageDistribution = self.get_object(pk)
        serializer = AgeDistributionSerializer(ageDistribution)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ageDistribution = self.get_object(pk)
        serializer = AgeDistributionSerializer(ageDistribution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ageDistribution = self.get_object(pk)
        ageDistribution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
