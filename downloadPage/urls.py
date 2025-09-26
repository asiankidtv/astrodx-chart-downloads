from django.urls import path, include
from downloadPage.views import index

urlpatterns = [
    path('', index)
]
