from django.urls import path

from .views import login
from .views import index

# Create your urls here.


urlpatterns = [
    path('', login, name='login'),
    path('index/', index, name='index')
]
