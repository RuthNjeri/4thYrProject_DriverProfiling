from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):

	ROLES_CHOICES = (

		('Insurance','Insurance Company'),
		('Sacco','Sacco'),
	)

	user = models.OneToOneField(User, unique =True, related_name='profile')
	business_name = models.CharField(max_length = 200, null=True)
	email = models.CharField(max_length=200,null=True)
	location = models.CharField(max_length=200,null=True)
	phone_number = models.CharField(max_length=200, null=True)
	role=models.CharField(max_length=200, null=True, choices= ROLES_CHOICES)
	entities=models.ForeignKey(User,blank=True,null=True,unique=False, related_name='entities')
	

@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,created,**kwargs):
	if created:
		UserProfile.objects.create(user=instance)



class HumanValidationData(models.Model):

	date = models.DateTimeField(max_length = 200, null=True)
	registration_number = models.CharField(max_length=200,null=True)
	route_number = models.CharField(max_length=200,null=True)
	from_location = models.CharField(max_length=200, null=True)
	to_location=models.CharField(max_length=200, null=True)
	start_time=models.CharField(max_length=200, null=True)
	end_time=models.CharField(max_length=200, null=True)
	event_type=models.CharField(max_length=200, null=True)
	event_description=models.CharField(max_length=200, null=True)
	fare=models.CharField(max_length=200, null=True)
	passengers=models.CharField(max_length=200, null=True)
	exact_time=models.CharField(max_length=200, null=True)
	latitude=models.CharField(max_length=200, null=True)
	longitude=models.CharField(max_length=200, null=True)
	altitude=models.CharField(max_length=200, null=True)





		