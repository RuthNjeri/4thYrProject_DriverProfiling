from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):

	ROLES_CHOICES = (

		('Insurance Company','Insurance Company'),
		('Sacco','Sacco'),
		('Matatu Owner', 'Matatu Owner'),


		)

	user = models.OneToOneField(User, unique =True)
	business_name = models.CharField(max_length = 200, null=True)
	email = models.CharField(max_length=200,null=True)
	location = models.CharField(max_length=200,null=True)
	phone_number = models.CharField(max_length=200, null=True)
	role=models.CharField(max_length=200,choices=ROLES_CHOICES, null=True)

	

@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,created,**kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
	instance.userprofile.save()
