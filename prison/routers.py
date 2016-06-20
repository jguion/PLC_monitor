from swampdragon import route_handler
from swampdragon.route_handler import ModelPubRouter
from .models import CellDoor
from .serializers import CellDoorSerializer


class CellDoorRouter(ModelPubRouter):
    valid_verbs = ['subscribe']
    route_name = 'cell_doors'
    model = CellDoor
    serializer_class = CellDoorSerializer


route_handler.register(CellDoorRouter)
