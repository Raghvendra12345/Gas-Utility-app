from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ServiceRequest

class CreateServiceRequestView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    fields = ['type', 'description', 'attachment']
    template_name = 'requests/create_request.html'
    success_url = '/requests/'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'requests/list_requests.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)

class ServiceRequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'requests/detail_request.html'
