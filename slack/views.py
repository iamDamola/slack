from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SlackSerializer
from .models import Slackdata

class SlackViewsets (viewsets.ModelViewSet):
    queryset = Slackdata.objects.all()
    serializer_class = SlackSerializer


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Slackdata.objects.filter(typ='details')
    serializer_class = SlackSerializer


# Create your views here.
