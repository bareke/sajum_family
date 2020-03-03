from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from .models import *
from .forms import OfficerForm


# Create your views here.


def login(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request, 'login.html')


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


class ProcessView(TemplateView):
    template_name = 'process.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'


class NotificationView(TemplateView):
    template_name = 'notification.html'


class OfficerCreateView(CreateView):
    model = Officer
    form_class = OfficerForm
    template_name = 'officer_form.html'
    success_url = '/officers/'


class OfficerDeleteView(DeleteView):
    model = Officer
    template_name = 'object_delete.html'
    success_url = '/officers/'


class OfficerDetailView(DetailView):
    model = Officer
    template_name = 'officer_list.html'


class OfficerListView(ListView):
    model = Officer
    template_name = 'officer_list.html'


class WhistleblowerCreateView(CreateView):
    model = Citizen
    # form_class = CitizenForm
    fields = '__all__'
    template_name = 'whistleblower_form.html'
    success_url = '/victim/add/'


class VictimCreateView(CreateView):
    model = Citizen
    # form_class = CitizenForm
    fields = '__all__'
    template_name = 'victim_form.html'
    success_url = '/hostess/add/'


class HostessCreateView(CreateView):
    model = Citizen
    # form_class = CitizenForm
    fields = '__all__'
    template_name = 'hostess_form.html'
    success_url = '/denounced/add/'


class DenouncedCreateView(CreateView):
    model = Citizen
    # form_class = CitizenForm
    fields = '__all__'
    template_name = 'denounced_form.html'
    success_url = '/fact/add/'


class FactCreateView(CreateView):
    model = Fact
    # form_class = CitizenForm
    fields = '__all__'
    template_name = 'fact_form.html'
    success_url = '/process/'
