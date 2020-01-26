from django.urls import path

from .views import index

# Create your urls here.


urlpatterns = [
    path('', index),
]
