from rest_framework import serializers
from .models import *

class MarketingBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingBrief
        fields = '__all__'