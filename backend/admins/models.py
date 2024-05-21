from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
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


# class MyUserManager(BaseUserManager):
#     def create_user(self, phone_number, password=None):
#         if not phone_number:
#             raise ValueError('The phone number must be set')
#         user = self.model(phone_number=phone_number)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, phone_number, password):
#         user = self.create_user(phone_number, password=password)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
# class MyUser(AbstractBaseUser):
#     phone_number = models.CharField(max_length=20, unique=True)
#     password = models.CharField(_("password"), max_length=128,null=True)
#     last_login = models.DateTimeField(_("last login"), blank=True, null=True,auto_now_add=timezone.now())
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     objects = MyUserManager()
#     USERNAME_FIELD = 'phone_number'
#     def __str__(self):
#         return self.phone_number
#     def has_perm(self, perm, obj=None):
#         return True
#     def has_module_perms(self, app_label):
#         return True
#     @property
#     def is_staff(self):
#         return self.is_admin
  



