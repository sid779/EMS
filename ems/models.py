from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Host(models.Model):
	host_name = models.CharField(max_length=200)
	email = models.EmailField()
	phone = models.CharField(max_length=12)


class Visitor(models.Model):
	def get_default_my_time():
  		return timezone.localtime(timezone.now())
	
	visitor_name = models.CharField(max_length=200)
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	checkin = models.TimeField(default = get_default_my_time)
	checkout = models.TimeField(default = get_default_my_time)
	host = models.CharField(max_length=200)

	def exit(self,time):
		if time==None:
			self.checkout = timezone.localtime(timezone.now())
		else:
			self.checkout = time
		self.save()

