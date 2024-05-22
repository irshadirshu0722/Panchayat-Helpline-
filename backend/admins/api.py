from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response
from service.models import Complaint
from service.serializers import ComplaintStatusSerializer
from django.utils import timezone
class ComplaintStatusChangeView(APIView):
  def put(self,request,id):
    try:
      instance = Complaint.objects.get(id=id)
      data = request.data
      data['_update_at'] = timezone.now()
      serializer = ComplaintStatusSerializer(instance,data=data,partial=True)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return  Response(status=status.HTTP_200_OK)
    except Complaint.DoesNotExist:
      return Response({'error':'Complaint not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
      return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)