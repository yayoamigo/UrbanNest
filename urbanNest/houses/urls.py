from django.urls import path
from . import views

urlpatterns = [
    path('houses/', views.HouseList.as_view()),
    path('houses/<int:pk>/', views.HouseDetail.as_view()),
]