from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import OTP
from .exceptions import *
from django.utils import timezone
from rest_framework.authtoken.models import Token

User = get_user_model()
class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
class LoginVerifySerializer(serializers.Serializer):
    token = serializers.UUIDField()
    otp =  serializers.CharField()
    phone_number = serializers.CharField()
    def validate(self, attrs):
        token = attrs.get('token')
        otp  = attrs.get('otp')
        number  = attrs.get('phone_number')
        otp_instance = OTP.objects.filter(token=token,phone_number=number).first()
        if not otp_instance:
          raise OTPNotExist
        if not otp_instance.is_valid():
          raise TokenExpired
        if otp_instance.otp != otp:
          raise OTPWrong
        return super().validate(attrs)
    def create(self, validated_data):
      data = self.validated_data
      phone_number = data['phone_number']
      user,created = User.objects.get_or_create(username=phone_number)
      user.last_login = timezone.now()
      user.save()
      return user
