from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib import messages
from log.models import UserProfile

# Create your views here.

#the decorator is not to allow any view without authenticating
@login_required(login_url = "login/")
def home(request):
	return render(request,"home.html")


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
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