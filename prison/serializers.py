from swampdragon.serializers.model_serializer import ModelSerializer


class CellDoorSerializer(ModelSerializer):
    class Meta:
        model = 'prison.CellDoor'
        publish_fields = ['unlocked', 'secured']
