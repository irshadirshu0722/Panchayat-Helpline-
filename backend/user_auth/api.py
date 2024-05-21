from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer,LoginVerifySerializer
from django.contrib.auth import get_user_model
from admins.models import OTP
from .utils import send_otp,generate_otp
from django.utils import timezone
User = get_user_model()

class LoginApiView(APIView):
  def post(self,request):
    serializer = LoginSerializer(data=request.data)
    try:
      if serializer.is_valid(raise_exception=True):
        phone_number = serializer.validated_data['phone_number']
        otp_code  = generate_otp()
        otp_instance,created = OTP.objects.update_or_create(defaults={'otp':otp_code},phone_number=phone_number)
        if not created:
          otp_instance.resetToken()
        send_otp(phone_number,otp_code)
        return Response({'token':otp_instance.token},status=status.HTTP_200_OK)
    except Exception as e:
      print(str(e))
      return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
class LoginVerifyApiView(APIView):
  def post(self,request):
    serializer = LoginVerifySerializer(data=request.data)
    try:
      if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        return Response({'auth_token':user.auth_token.key},status=status.HTTP_200_OK)
    except Exception as e:
      print(str(e))
      return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)



