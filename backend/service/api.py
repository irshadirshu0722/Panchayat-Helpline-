from rest_framework.views import APIView
from .serializers import HelplineSerializer,ComplaintSerializer
from .models import Helpline
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Complaint
class HelplineApiView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self,request):
    helpline_instance = Helpline.objects.all()
    serializer = HelplineSerializer(helpline_instance,many=True)
    return Response({'data':serializer.data},status=status.HTTP_200_OK)

class ComplaintApiView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self,request):
    complaints = Complaint.objects.filter(user=request.user)
    serializer = ComplaintSerializer(complaints,many=True)
    return Response({'data':serializer.data},status=status.HTTP_200_OK)
  def post(self,request):
    serializer = ComplaintSerializer(data=request.data,context={'request': request})
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
    return Response({},status=status.HTTP_200_OK)