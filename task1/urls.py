from django.urls import path
from .views import task1

urlpatterns = [
    path('', task1, name='task1'),
]
