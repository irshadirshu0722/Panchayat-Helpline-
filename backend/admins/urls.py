from django.urls import path
from .api import ComplaintStatusChangeView
urlpatterns = [
  path('complaint/status/<int:id>/',ComplaintStatusChangeView.as_view() ,name='complaint-status-change-vide'),
]