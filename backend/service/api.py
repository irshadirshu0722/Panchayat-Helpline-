from rest_framework.views import APIView
from .serializers import HelplineSerializer
from .models import Helpline
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
class HelplineApiView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self,request):
    helpline_instance = Helpline.objects.all()
    serializer = HelplineSerializer(helpline_instance,many=True)
    return Response({'data':serializer.data},status=status.HTTP_200_OK)