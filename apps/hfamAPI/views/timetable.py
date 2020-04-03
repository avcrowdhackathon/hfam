from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hfamAPI.models.timetable import TimeTable
from apps.hfamAPI.serializers.timetable import TimeTableSerializer


# /timetables
class TimeTableList(APIView):
    """
    List all TimeTables, or create a new TimeTable.
    """

    def get(self, request):
        timetables = TimeTable.objects.all()
        serializer = TimeTableSerializer(timetables, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Creates an Age Distribution", request_body=TimeTableSerializer)
    def post(self, request):
        serializer = TimeTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# /timetables/{id}
class TimeTableDetail(APIView):
    """
    Retrieve, update or delete a TimeTable instance.
    """

    def get_object(self, pk):
        try:
            return TimeTable.objects.get(pk=pk)
        except TimeTable.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        timetable = self.get_object(pk)
        serializer = TimeTableSerializer(timetable)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        timetable = self.get_object(pk)
        serializer = TimeTableSerializer(timetable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        timetable = self.get_object(pk)
        timetable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
