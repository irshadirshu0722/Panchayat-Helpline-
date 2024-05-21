from rest_framework import serializers
from .models import *


class HelplineImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = HelplineImage
    fields = ('image_url',)

class HelplineSerializer(serializers.ModelSerializer):
  images = HelplineImageSerializer(many=True)
  class Meta:
    model=Helpline
    fields = '__all__'