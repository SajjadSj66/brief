from django.urls import path, include
from .views import *
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'individual', IndividualInformationViewSet, basename='individual')
routers.register(r'purpose', PurposeAdvertisingViewSet, basename='purpose')
routers.register(r'market', MarketShareViewSet, basename='market')
routers.register(r'brand', BrandPositionViewSet, basename='brand')
routers.register(r'target', TargetViewSet, basename='target')
routers.register(r'budget', BudgetViewSet, basename='budget')
routers.register(r'request', RequestViewSet, basename='request')

urlpatterns = [
    path('api/',include(routers.urls)),
]
