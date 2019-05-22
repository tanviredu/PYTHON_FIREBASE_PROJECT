## this is a auth app which will used in django
## using firebase for less server side coding
## using the GOOGLE API

import pyrebase

## confidential of the account
config = {
    "apiKey": "AIzaSyByKG6cCG-CrMz4-D1ENO8YtGtLZ_vNW8M",
    "authDomain": "fir-djangoauth.firebaseapp.com",
    "databaseURL": "https://fir-djangoauth.firebaseio.com",
    "projectId": "fir-djangoauth",
    "storageBucket": "fir-djangoauth.appspot.com",
    "messagingSenderId": "522252525789"
  };
firebase_obj = pyrebase.initialize_app(config);
## connecting to the firebase
#print (firebase_obj)
##connection successful
## we use the auth function of the firebase_obj
auth = firebase_obj.auth()


#we create the user using gmail
## taking the input from the html page


## this is for test we use the web form to grab email and password
status = int(input("=>"))
if status==1:

    try:
        email =input("Enter your email\n=>")
        password =input("Enter your password\n=>")
        user = auth.create_user_with_email_and_password(email,password)
        tok = auth.get_account_info(user['idToken'])
        #print(tok)
        ## we can verify the account by sending email
        auth.send_email_verification(user['idToken'])
        ## we can reset the email password if user forget it
        auth.send_password_reset_email(email)
    except:
        print ("User already exists")
elif status==2:
    try:
        email =input("Enter your email\n=>")
        password =input("Enter your password\n=>")
        login_user = auth.sign_in_with_email_and_password(email,password)
        tok = auth.get_account_info(login_user['idToken'])
        print(tok)
        print("login Successful")
    except:
        print("Problem")
    
else:
    print ("invalid option")