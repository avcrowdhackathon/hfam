from rest_framework import serializers

from apps.hfamAPI.models.inventory import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["id", "masks", "gloves", "ventilators"]
