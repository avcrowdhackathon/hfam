from rest_framework import serializers

from apps.hfamAPI.models.timetable import TimeTable


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = ["id"]
