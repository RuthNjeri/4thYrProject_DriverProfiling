from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Drivers(models.Model):
	user = models.ForeignKey(User,blank =True,null=True,unique=False)
	name = models.CharField(max_length=200,null=True)
	id_number=models.CharField(max_length=200,null=True)
	phone_number=models.CharField(max_length=200,null=True)
	vehicle_reg=models.CharField(max_length=200,null=True)