from django.urls import path
from .views import PersonAPIView

urlpatterns = [
    path('person', PersonAPIView.as_view()),
    path('person/<str:pk>', PersonAPIView.as_view()) # To capture ids
]