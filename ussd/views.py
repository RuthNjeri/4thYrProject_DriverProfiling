# Create your views here.
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)
from ussd.config import username,apikey
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from ussd.models import Drivers
from log.models import HumanValidationData
from django.db.models import Sum, F
# Create your views here.
@csrf_exempt
def ussd(request):



	if request.method == 'POST'and request.POST:

		sessionId = request.POST.get('sessionId')
		serviceCode=request.POST.get('serviceCode')
		phoneNumber=request.POST.get('phoneNumber')
		text=request.POST.get('text')
		now = datetime.datetime.now()


		textList= text.split('*')
		userResponse= textList[-1].strip()

		



		try:

			result,created = Drivers.objects.get_or_create(phone_number=phoneNumber)
			if created:
			   result.save()

			
					 # check if user is available and serve menu, if not register
			if result and result.name and result.id_number and result.vehicle_reg:

				if text=="":
					#serve the services menu
					response = "CON Welcome to Barabara Ulinzi, Choose a language/Chagua lugha.\n"
					response += " 1. English.\n"
					response += " 2. Kiswahili.\n"


					return HttpResponse(response, content_type='text/plain')


				if text == '1':

														
					response = "CON Please select a service.\n"
					response += "1. View my driving report.\n"
					response += "2. Help.\n"

					return HttpResponse(response, content_type='text/plain')

				if text == '1*1':

					user = Drivers.objects.get(phone_number=phoneNumber)
					amount =HumanValidationData.objects.filter(registration_number=user.vehicle_reg).aggregate(amount=Sum(F('passengers')*F('fare')))
					fare = [amount for amount in amount.values()]
					
					passengers = HumanValidationData.objects.filter(registration_number=user.vehicle_reg).aggregate(Sum('passengers'))
					for value in passengers.values():
						
									
						response = "END Your Report:\n"
						response += "1. You have had ["+str(value)+"] PASSENGERS in total.\n"
						response += "2. The total amount of FARE collected is Ksh "+str(fare)+"."
						

					return HttpResponse(response, content_type='text/plain')	

				if text == '1*2':

						response = "END Help:\n"
						response += "send the keyword HELP to 2284. You can also reach us at +254727584378\n"

						

						return HttpResponse(response, content_type='text/plain')	

				if text == '2':

														
					response = "CON Tafadhali chagua nabari yeyote.\n"
					response += "1. Angalia ripoti yangu barabarani.\n"
					response += "2. Usaidizi.\n"

					return HttpResponse(response, content_type='text/plain')

				if text == '2*1':

					user = Drivers.objects.get(phone_number=phoneNumber)
					amount =HumanValidationData.objects.filter(registration_number=user.vehicle_reg).aggregate(amount=Sum(F('passengers')*F('fare')))
					fare = [amount for amount in amount.values()]
					
					passengers = HumanValidationData.objects.filter(registration_number=user.vehicle_reg).aggregate(Sum('passengers'))
					for value in passengers.values():
						
									
						response = "END Ripoti Yako:\n"
						response += "1. Umebeba abiria ["+str(value)+"].\n"
						response += "2. Umepokea pesa kutoka abiria Shillingi "+str(fare)+"."
						

					return HttpResponse(response, content_type='text/plain')

				if text == '2*2':

						response = "END Help:\n"
						response += "Tuma jina USAIDIZI kwa 2284. Tupigie simu kwa nambari +254727584378\n"

						

						return HttpResponse(response, content_type='text/plain')		

			else:
				
				if created: #chek if user is in the microfinance tabe
						
						result.save()#save the user
						response= "CON Please enter your name/jina"
						
	  
						return HttpResponse(response, content_type='text/plain')

				if not created:
						if not result.name:
						   #save the name
						   result.name = userResponse
						   result.save()

						
						   response= "CON Please enter your ID number"
						 
						   return HttpResponse(response, content_type='text/plain')
						if not result.id_number:
						 #save the id number
						   result.id_number = userResponse
						   result.save()

						
						   response ="CON Please enter your Vehicle number plate"
						   return HttpResponse(response, content_type='text/plain')	

						if not result.vehicle_reg:
						 #save the vehicle number
						   result.vehicle_reg = userResponse
						   result.save()

						   response ="END Your registration was successful!"
						   return HttpResponse(response, content_type='text/plain')	

		except Exception as e:

			 print('exception', e)


			 #11g. Request for city again
			 response = "END Apologies, something is wrong... \n"

			 # Print the response onto the page so that our gateway can read it
			 return HttpResponse(response, content_type='text/plain')

			