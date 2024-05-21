from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
import datetime
User = get_user_model()
# Create your models here.
def upload_to(instance, filename):
    today = datetime.now().strftime('%d-%m-%Y')
    return f'complaints/date-{today}/{filename}'

class Complaint(models.Model):
  PROBLEM_RATE_CHOICES = [(str(i), str(i)) for i in range(1, 11)]
  ward = models.IntegerField()
  name = models.IntegerField()
  user = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='complaints',null=True)
  subject = models.CharField(max_length=100)
  description = models.TextField()
  landmark = models.CharField(max_length=500)
  problem_rate = models.CharField(max_length=10,choices=PROBLEM_RATE_CHOICES)
  audio = CloudinaryField(resource_type='audio', format='mp3',folder=upload_to)
  @property
  def audio_url(self):
      return self.audio.url

class ComplaintImage(models.Model):
  image = CloudinaryField(resource_type='image', format='jpg',folder=upload_to)
  complaint = models.ForeignKey(Complaint,on_delete=models.CASCADE,related_name='images')
  @property
  def image_url(self):
    return self.image.url

class Helpline(models.Model):
  TYPE_CHOICES = [('hospital','Hospital'),('fire_station','Fire Station'),('police_station','Police Station')]
  type = models.CharField(max_length=100,choices=TYPE_CHOICES)
  location_url = models.CharField(max_length=500)
  title = models.CharField(max_length=100)
  description = models.TextField()
class HelplineImage(models.Model):
  image = CloudinaryField(resource_type='image', format='jpg',folder='helpline/images')
  helpline = models.ForeignKey(Helpline,on_delete=models.CASCADE,related_name='images')
  @property
  def image_url(self):
    return self.image.url