from rest_framework import serializers
from .models import *

class IndividualInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualInformation
        fields = '__all__'

class PurposeAdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurposeAdvertising
        fields = '__all__'

class MarketShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketShare
        fields = '__all__'

class BrandPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandPosition
        fields = '__all__'

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'