from django.shortcuts import render
from django.views.generic import ListView
from .models import CellDoor


class CellDoors(ListView):
    model = CellDoor
    template_name = 'home.html'

    def get_queryset(self):
        return self.model.objects.order_by('-pk')
