from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from django.shortcuts import render

def calendar_view(request):
    return render(request, 'scheduler_app/calendar.html')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer