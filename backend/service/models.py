from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.utils import timezone
User = get_user_model()
# Create your models here.
def upload_to(instance):
    print(instance)
    today = timezone.now().strftime('%d-%m-%Y')
    date = '_'.join(today.split('-')) 
    return f''

class Complaint(models.Model):
  PROBLEM_RATE_CHOICES = [(str(i), str(i)) for i in range(1, 11)]
  STATUS_CHOICES = [('pending','Pending'),('rejected','Rejected'),('approved','Approved')]
  ward = models.IntegerField()
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='complaints',null=True)
  subject = models.CharField(max_length=100)
  description = models.TextField()
  landmark = models.CharField(max_length=500)
  problem_rate = models.CharField(max_length=10,choices=PROBLEM_RATE_CHOICES)
  audio = CloudinaryField(resource_type='auto',folder='complaints/audio',null=True,blank=True)
  status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
  _update_at = models.DateTimeField(null=True)
  _complaint_at = models.DateTimeField(auto_now_add=True,null=True)
  @property
  def update_at(self):
    if(self._update_at):
      return self._update_at.strftime("%d %b %Y") 
    else:
      return "---"
  @property
  def complaint_at(self):
    return self._complaint_at.strftime("%d %b %Y") 
  @property
  def audio_url(self):
      return self.audio.url
class ComplaintImage(models.Model):
  image = CloudinaryField(format='jpg',folder='complaints/image')
  complaint = models.ForeignKey(Complaint,on_delete=models.CASCADE,related_name='images')
  @property
  def image_url(self):
    return self.image.url
  def __str__(self) -> str:
     return 'file'

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