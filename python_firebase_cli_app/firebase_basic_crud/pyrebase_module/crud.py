## this app is using the pyrebase Module 
## for better performence
## from my point of view pyrebase is better for 
## python and fire base
# for the database or auth or storage 
#first init the app
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
auth = firebase_obj.auth()
## for database you have to be a user first
email = input("email=>\n")
password = input("password=>\n")
user = auth.sign_in_with_email_and_password(email, password)
## init the database
db=firebase_obj.database()

##if we want to store the database
## we have to do it with a dict


################## most important method######################
##############################################################
#############################################################
##########################################################
## set the data
## if you want to create your own key set() is the method
data1 = {'name':'morty'}
db.child('user').child('name').set(data1)


##do not do the following because if you do then all the data in the 
##tree user will be replaced by it so always create a new branch
## so it means create a new user with a new subtree
data1 = {'name':'mortyparent'}
db.child('user').set(data1)

#it will replace the user data with data1
###############################################
###############################################
##this is how we store userdefined token 
## update the data
db.child('user').child('name').update({'name':'Tanvir'})
##############################################
####perfect way and more optimize
####remove the data
db.child('user').child('name').remove()
#####



################################################
#############################################
#remember we access the data by the child() method
#we go from child to child and then update() and remove()
## we set the data in dict and with our disered position in dict


###### how to get the data
## to find all the data in a tree

all_user = db.child('user').get()
## one method

print(all_user.val())
##other method
for user in all_user.each():
    print (str(user.key())+" "+str(user.val()))

## thats all
###########we can use th fire store to store jpg.its another topic
