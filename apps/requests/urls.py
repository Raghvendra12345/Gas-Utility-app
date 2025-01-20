from django.urls import path
from .views import CreateServiceRequestView, ServiceRequestListView, ServiceRequestDetailView

urlpatterns = [
    path('create/', CreateServiceRequestView.as_view(), name='create_request'),
    path('', ServiceRequestListView.as_view(), name='list_requests'),
    path('<int:pk>/', ServiceRequestDetailView.as_view(), name='detail_request'),
]
