
from django.contrib import admin
from django.urls import path
from .api import HelplineApiView
urlpatterns = [
  path('helpline/',HelplineApiView.as_view(),name='help-line')
]
