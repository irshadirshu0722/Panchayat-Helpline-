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
class ComplaintImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = ComplaintImage
    fields = ('image_url',)
class ComplaintSerializer(serializers.ModelSerializer):
    images = ComplaintImageSerializer(many=True,read_only=True)
    upload_images = serializers.FileField(write_only=True)
    audio_url = serializers.SerializerMethodField(read_only=True)
    complaint_at = serializers.SerializerMethodField(read_only=True)
    update_at = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Complaint
        exclude = ('_complaint_at','_update_at',)
    def get_audio_url(self,obj):
      return obj.audio_url
    def get_complaint_at(self,obj):
      return obj.complaint_at
    def get_update_at(self,obj):
      return obj.update_at
    def create(self, validated_data):
        images_data = self.context.get('request').FILES.getlist('upload_images')
        validated_data.pop('upload_images')
        complaint = Complaint.objects.create(**validated_data)
        for image_data in images_data:
            ComplaintImage.objects.create(complaint=complaint, image=image_data)
        return complaint
    def save(self, **kwargs):
        user = kwargs.get('user')
        print(self.validated_data)
        self.validated_data['user'] = user
        return super().save(**kwargs)
    


class ComplaintStatusSerializer(serializers.ModelSerializer):
   class Meta:
      model = Complaint
      fields = ('status','_update_at',)