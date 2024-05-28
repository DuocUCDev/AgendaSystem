from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchedulesViewSet

router = DefaultRouter()
router.register('schedules', SchedulesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]