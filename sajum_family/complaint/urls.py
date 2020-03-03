from django.urls import path

from .views import login
from .views import IndexView
from .views import DashboardView
from .views import ProcessView
from .views import ProfileView
from .views import NotificationView
from .views import OfficerCreateView
from .views import OfficerListView
from .views import OfficerDetailView
from .views import OfficerDeleteView

from .views import WhistleblowerCreateView
from .views import VictimCreateView
from .views import HostessCreateView
from .views import DenouncedCreateView
from .views import FactCreateView


# Create your urls here.

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', login, name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('process/', ProcessView.as_view(), name='process'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('notification/', NotificationView.as_view(), name='notification'),
    path('officer/add/', OfficerCreateView.as_view(), name='officer-add'),
    path('officer/detail/<int:pk>', OfficerDetailView.as_view(), name='officer-detail'),
    path('officer/delete/<int:pk>', OfficerDeleteView.as_view(), name='officer-delete'),
    path('officers/', OfficerListView.as_view(), name='officers'),

    path('whistleblower/add/', WhistleblowerCreateView.as_view(), name='whistleblower-add'),
    path('victim/add/', VictimCreateView.as_view(), name='victim-add'),
    path('hostess/add/', HostessCreateView.as_view(), name='hostess-add'),
    path('denounced/add/', DenouncedCreateView.as_view(), name='denounced-add'),
    path('fact/add/', FactCreateView.as_view(), name='fact-add'),
]
