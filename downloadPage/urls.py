from django.urls import path
from downloadPage.views import index, download

urlpatterns = [
    path('', index),
    path('download/<str:name>/', download)
]
