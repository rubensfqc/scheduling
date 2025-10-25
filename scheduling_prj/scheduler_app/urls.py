# scheduler/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, calendar_view

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('calendar/', calendar_view, name='calendar'),
    #path('api/', include('scheduler_app.urls')),
]
