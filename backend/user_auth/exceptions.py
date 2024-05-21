from rest_framework.exceptions import APIException
class OTPNotExist(APIException):
  status_code = 400
  default_detail = 'Otp is wrong try again later'
class OTPWrong(APIException):
  status_code = 400
  default_detail = 'Please enter correct otp'
class TokenExpired(APIException):
  status_code = 400
  default_detail = 'Token expired, please try again'



