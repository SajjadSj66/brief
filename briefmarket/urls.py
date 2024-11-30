from django.urls import path
from .views import *

urlpatterns = [
    path('briefs/', MarketingBriefCreateListAPIView.as_view()),
    path('briefs/<int:pk>', MarketingBriefRetrieveUpdateAPIView.as_view()),
]
