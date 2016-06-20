from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import CellDoorSerializer


class CellDoor(SelfPublishModel, models.Model):
    serializer_class = CellDoorSerializer
    door_number = models.IntegerField()
    unlocked = models.BooleanField()
    secured = models.BooleanField()
