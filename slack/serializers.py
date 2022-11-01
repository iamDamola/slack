from rest_framework import serializers
from .models import Slackdata

class SlackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slackdata
        fields = ['id','username','backend','age','bio']