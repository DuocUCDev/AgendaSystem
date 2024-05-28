from rest_framework import viewsets
from .models import Schedules
from .serializers import SchedulesSerializer

# Create your views here.
class SchedulesViewSet(viewsets.ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer