from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
import pyrebase
## django has built in form so that we can use it

from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
	return render(request,'fire/index.html',{})

def login_user(request):

    if request.method =='POST':
        ## this ios confidential
        config = {
            "apiKey": "AIzaSyByKG6cCG-CrMz4-D1ENO8YtGtLZ_vNW8M",
            "authDomain": "fir-djangoauth.firebaseapp.com",
            "databaseURL": "https://fir-djangoauth.firebaseio.com",
            "projectId": "fir-djangoauth",
            "storageBucket": "fir-djangoauth.appspot.com",
            "messagingSenderId": "522252525789"}
        import pyrebase
        firebase_obj = pyrebase.initialize_app(config)
        auth = firebase_obj.auth()  ## create the auth obj of firebase
        ## fetch the parameter of the user
        email = request.POST['email']
        password = request.POST['password']
        ##try to login with the user
        try:
            login_user = auth.sign_in_with_email_and_password(email,password)

            token =auth.get_account_info(login_user['idToken'])
            #messages.success(request,('you have successfully loged in.your access token is genareted'+str(token)))

            return render(request,'fire/success.html')
        except:
            messages.success(request,('sorry cant login no access token is generated'))
            return render(request,'fire/success.html')


		# ok now we get the data
		## first comes the
	#	##
	#	if user is None:
	#		messages.success(request,('problem using loggin in'))
	#		return redirect('login')
	#	else:
	#		login(request,user)  ## this will log you in the main django administration
	#		#to send a confirmation messages
	#		messages.success(request,('you have successfully loged in'))

	#		return redirect('index')
    else:
        return render(request,'fire/login.html',{})




def create_user(request):

    if request.method =='POST':
        ## this ios confidential
        config = {
            "apiKey": "AIzaSyByKG6cCG-CrMz4-D1ENO8YtGtLZ_vNW8M",
            "authDomain": "fir-djangoauth.firebaseapp.com",
            "databaseURL": "https://fir-djangoauth.firebaseio.com",
            "projectId": "fir-djangoauth",
            "storageBucket": "fir-djangoauth.appspot.com",
            "messagingSenderId": "522252525789"}
        import pyrebase
        firebase_obj = pyrebase.initialize_app(config)
        auth = firebase_obj.auth()  ## create the auth obj of firebase
        ## fetch the parameter of the user
        email = request.POST['email']
        password = request.POST['password']
        ##try to login with the user
        try:
            user = auth.create_user_with_email_and_password(email,password)

            token =auth.get_account_info(user['idToken'])
            messages.success(request,('you have successfully registered '))
            #send a two way authentication
            #auth.send_email_verification(user['idToken'])
            return render(request,'fire/success.html')
        except:
            messages.success(request,('sorry cant registered'))
            return render(request,'fire/success.html')


		# ok now we get the data
		## first comes the
	#	##
	#	if user is None:
	#		messages.success(request,('problem using loggin in'))
	#		return redirect('login')
	#	else:
	#		login(request,user)  ## this will log you in the main django administration
	#		#to send a confirmation messages
	#		messages.success(request,('you have successfully loged in'))

	#		return redirect('index')
    else:
        return render(request,'fire/register.html',{})

