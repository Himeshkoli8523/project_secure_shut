import pyrebase
from firebase import firebase
import check_email
import requests
from kivy.app import App

config = {
"apiKey": "AIzaSyDl_ex7CRrUXRfncH90qGcZM1qLyTFORJo",
"authDomain": "shut-6276a.firebaseapp.com",
"databaseURL": "https://shut-6276a-default-rtdb.firebaseio.com",
"projectId": "shut-6276a",
"storageBucket": "shut-6276a.appspot.com",
"messagingSenderId": "827204186735",
"appId": "1:827204186735:web:ac5961cfb361786625139a",
"measurementId": "G-G50ZJD9S5F"
}

firebase_auth = pyrebase.initialize_app(config)

firebase_data = firebase.FirebaseApplication("https://shut-6276a-default-rtdb.firebaseio.com/" , None)

class MyFirebase() :
    def sign_up(self , fullname , email , password):
        if check_email.check(email) == True:
            try :
                
                # RealTime Database
                data = {
                    "Name": fullname,
                    "Email": email,
                    "Password": password
                }
                result = firebase_data.post("https://shut-6276a-default-rtdb.firebaseio.com/", data) 

                # Creating User
                signup_auth = firebase_auth.auth()
                user_signup = signup_auth.create_user_with_email_and_password(email, password)
                print("SignUp Successfully")
                
                App.get_running_app().root.ids["signup_screen"].ids["signup_screen"].text = "[b][color=#FF0000]Signup Succesfully.[/color][/b]"
            except requests.HTTPError as e:
                App.get_running_app().root.ids["signup_screen"].ids["signup_screen"].text = "[b][color=#0000FF]{}[/color][/b]".format(e)
        else:
            App.get_running_app().root.ids["signup_screen"].ids["signup_screen"].text = "[b][color=#FF0000]Invalid Email.[/color][/b]"



    def sign_in(self , email , password):
        signin_auth = firebase_auth.auth()

        try :
            user_login = signin_auth.sign_in_with_email_and_password(email,password)
            print("Login Successfully !!!")
            print(user_login["registered"])
            path_to_home = user_login["registered"]

            if path_to_home == True :
                print("hello")
                App.get_running_app().root.ids["login_screen"].ids["login_message"].text = ""
                App.get_running_app().change_screen("home_screen")
                App.get_running_app().root.ids["home_screen"].ids["passing_email"].text = "[b]%s[/b]" %email

        except :
            App.get_running_app().root.ids["login_screen"].ids["login_message"].text = "[b]Invalid Email or Password[/b]"


    def forgot_password(self , email) :
        try:
            auth = firebase_auth.auth()
            auth.send_password_reset_email(email)
            App.get_running_app().root.ids["forgot_password_screen"].ids["forgot_message"].text = "[b]Thanks! Please check your email .[/b]"
        except:
            App.get_running_app().root.ids["forgot_password_screen"].ids["forgot_message"].text = "[b][color=#FF0000]Please Enter Correct Email !.[/color][/b]"
