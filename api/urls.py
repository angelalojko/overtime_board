from django.urls import path 
from .views import get_overtime


urlpatterns = [
    path('overtime/', get_overtime)
]