from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('samples/', SampleListView.as_view(), name='sample_list'),
    path('samples/<int:pk>/', SampleDetailView.as_view(), name='sample_detail'),
]
