from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Complaint)
admin.site.register(ComplaintImage)
admin.site.register(Helpline)
admin.site.register(HelplineImage)