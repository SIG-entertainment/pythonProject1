from django.urls import path
from .views import ProductsList, PoductDetail

urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>', PoductDetail.as_view()),
]