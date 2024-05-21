
from django.contrib import admin
from django.urls import path
from .api import HelplineApiView,ComplaintApiView
urlpatterns = [
  path('helpline/',HelplineApiView.as_view(),name='help-line'),
  path('complaints/',ComplaintApiView.as_view(),name='complaint')
]
