
from django.contrib import admin
from django.urls import path
from .api import LoginApiView,LoginVerifyApiView
urlpatterns = [
  path('login/',LoginApiView.as_view(),name='login-api'),
  path('login/verify/',LoginVerifyApiView.as_view(),name='login-verify-api'),
]
