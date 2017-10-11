import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import serializers


from .forms import ProfileForm
from log.models import UserProfile
from ussd.models import Drivers
from log.models import HumanValidationData


# Create your views here.

#the decorator is not to allow any view without authenticating
@login_required(login_url = "login/")
def home(request):


	
	availableDrivers= Drivers.objects.filter(user=request.user)
	availableSacco = UserProfile.objects.filter(entities=request.user)
	

	return render(request,"home.html",{
		 'available': availableDrivers ,'sacco': availableSacco
	})

def vehicle_details(request, vehiclereg):
	vehicle_details= HumanValidationData.objects.filter(registration_number__iexact=vehiclereg)
	serialized_obj = serializers.serialize('json',vehicle_details)
	return JsonResponse(json.loads(serialized_obj),safe=False)

def driver_details(request, vehiclereg):
	driver_details= Drivers.objects.filter(vehicle_reg__iexact=vehiclereg)
	sacco = UserProfile.objects.filter(user=driver_details.first().user).first()

	serialized_obj = serializers.serialize('json',driver_details)
	response = {}
	response['driver_details']= json.loads(serialized_obj)

	response['sacco']= sacco.business_name
	return JsonResponse(response,safe=False)	

def sacco_details(request, pk):
	sacco_vehicles = Drivers.objects.filter(user_id=pk)
	serialized_obj = serializers.serialize('json', sacco_vehicles)
	return JsonResponse(json.loads(serialized_obj),safe=False)


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			messages.success(request,'Please choose a role')
			return redirect('profile')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})


@login_required
def update_profile(request):
	
	exists = UserProfile.objects.filter(user=request.user).exists()
	if exists:
		profile_data = UserProfile.objects.get(user=request.user)
	if request.method == 'POST':
		profile_form = ProfileForm(request.POST)
		if profile_form.is_valid():
			if exists:
				UserProfile.objects.filter(user=request.user).update(**profile_form.cleaned_data)
			else:
				profile = profile_form.save(commit=False)
				profile.user=request.user
				profile.save()
			messages.success(request, 'Your profile was successfully updated!')
			return redirect('profile')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		if exists:	
			profile_form = ProfileForm(initial=profile_data.__dict__)
		else:
			profile_form = ProfileForm()	
	return render(request, 'profile.html', {
		'profile_form': profile_form
	})


def drivers(request):
	if request.method=='POST':

		registration= request.POST.get('registration')
		Drivers.objects.filter(vehicle_reg__iexact=registration).update(user=request.user)
		return redirect('drivers')

	
	availableDrivers= Drivers.objects.filter(user=None)
	drivers = Drivers.objects.filter(user=request.user)
	

	return render(request,"drivers.html",{
		'donda': drivers, 'available': availableDrivers 
	})

def delete_driver(request,pk):
	Drivers.objects.filter(pk=pk).update(user=None)
	return redirect('drivers')





def sacco(request):
	if request.method=='POST':

		registration= request.POST.get('registration')
		UserProfile.objects.filter(business_name=registration).update(entities=request.user)
		return redirect('sacco')

	sacco= UserProfile.objects.filter(role='Sacco')
	savedSacco = UserProfile.objects.filter(entities=request.user)

	return render(request,"sacco.html",{
		'sacco':sacco, 'savedSacco': savedSacco
		})

def delete_sacco(request,pk):
	UserProfile.objects.filter(pk=pk).update(entities=None)
	return redirect('sacco')	


def driverProfile(request):
	
	driver = Drivers.objects.filter(user=request.user)
	sacco = UserProfile.objects.filter(entities=request.user)


	return render(request, "driverProfile.html",{
		'drivers': driver, 'sacco': sacco
		
	})