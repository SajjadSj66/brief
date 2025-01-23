from rest_framework import viewsets
from .models import *
from .serializers import *


# ViewSet برای اطلاعات فردی
class IndividualInformationViewSet(viewsets.ModelViewSet):
    queryset = IndividualInformation.objects.all()
    serializer_class = IndividualInformationSerializer

# ViewSet برای اهداف تبلیغاتی
class PurposeAdvertisingViewSet(viewsets.ModelViewSet):
    queryset = PurposeAdvertising.objects.all()
    serializer_class = PurposeAdvertisingSerializer

# ViewSet برای سهم بازار
class MarketShareViewSet(viewsets.ModelViewSet):
    queryset = MarketShare.objects.all()
    serializer_class = MarketShareSerializer

# ViewSet برای جایگاه برند
class BrandPositionViewSet(viewsets.ModelViewSet):
    queryset = BrandPosition.objects.all()
    serializer_class = BrandPositionSerializer

# ViewSet برای اهداف مالی و برند
class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

# ViewSet برای بودجه و مخاطبان
class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

# ViewSet برای درخواست
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
