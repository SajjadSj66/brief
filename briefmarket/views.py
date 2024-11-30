from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MarketingBriefCreateListAPIView(generics.ListCreateAPIView):
    queryset = MarketingBrief.objects.all()
    serializer_class = MarketingBriefSerializer
    # permission_classes = [IsAuthenticated]


class MarketingBriefRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = MarketingBrief.objects.all()
    serializer_class = MarketingBriefSerializer
