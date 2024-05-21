from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


import uuid
# Create your models here.
class OTP(models.Model):
  token = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
  phone_number = models.CharField(max_length=20,unique=True)
  otp = models.CharField(max_length=5)
  created_at = models.DateTimeField(auto_now_add=True)
  is_verified = models.BooleanField(default=False)
  def is_valid(self):
    return self.created_at >= timezone.now() - timedelta(minutes=10)
  def __str__(self):
    return f'{self.phone_number} - {self.otp}'
  def resetToken(self):
    self.token = uuid.uuid4()
    self.created_at = timezone.now()
    self.save()
# class CustomUserManager(BaseUserManager):
#   def login(self):
#     self.

class MyUser(AbstractBaseUser):
  phone_number = models.CharField(max_length=20,unique=True)
  USERNAME_FIELD = 'phone_number'


