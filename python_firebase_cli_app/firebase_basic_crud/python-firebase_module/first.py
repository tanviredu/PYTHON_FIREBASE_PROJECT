def get_password(username):
    ## get data
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://fir-djangoauth.firebaseio.com/', None)
    result = firebase.get('/user',username)
    print (result)
get_password('Tanvir')

def put_data():
    ## put data
    from firebase import firebase
    #new_user = "pirate"
    firebase = firebase.FirebaseApplication('https://fir-djangoauth.firebaseio.com/', None)
    result1 =firebase.post('/user','preety_hello')
    ## bellow there is child input dictonary inside a dict means child data
    result =firebase.post('/user','pirate',{'tpb':{'hello_tanvir':'password'}})

put_data() 

def put_password(password):
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://fir-djangoauth.firebaseio.com/', None)
    result = firebase.post('/user',password)
    return result
def delete_info():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://fir-djangoauth.firebaseio.com/', None)
    result = firebase.delete('/user','1')
    return result
delete_info()
    


put_password("1122")
