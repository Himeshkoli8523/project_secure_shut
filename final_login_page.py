from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import requests
import firebase_admin
import firebase
from firebase_admin import credentials


class MyApp(App):
    
    firebase_url = "https://shut-6276a-default-rtdb.firebaseio.com/.json"
    firebase = firebase.FirebaseApplication(firebase_url, None)
    my_api_key = 'AIzaSyDl_ex7CRrUXRfncH90qGcZM1qLyTFORJo'
    cred = credentials.Certificate("path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    def build(self):
        return MyBoxLayout()

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10

        self.add_widget(Label(
            text='Welcome\nTo\nSecureShut',
            color=[0, 0, 1, 1],  # for blue color
            font_size=30,
            halign='center'
        ))

        self.add_widget(Label(
            text='Sign in',
            font_size=20,
            halign='center'
        ))
        
        # Email input field
        self.email_input = TextInput(
            multiline=False,
            hint_text='Enter Email',
            padding_y=(10, 0),
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.email_input)
        
        # Password input field
        self.password_input = TextInput(
            multiline=False,
            password=True,
            hint_text='Enter Password',
            padding_y=(10, 0),
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.password_input)

        # Forgot Password button
        self.add_widget(Button(
            text='Forgot Password',
            on_press=self.forgot_password
        ))

        # Login button
        self.add_widget(Button(
            text='Login',
            on_press=self.login
        ))

        # Signup button
        self.ids['signup_button'] = Button(
            text='Sign up',
            font_size=20,
            on_press=self.signup
        )
        self.add_widget(self.ids['signup_button'])

    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        
        # Here, you would send a request to Firebase Authentication endpoint for sign-in
        # You can use the 'requests' library to make HTTP POST request to Firebase Authentication REST API
        # Example:
        response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=my_api_key', data={'email': email, 'password': password, 'returnSecureToken': True})
        # You need to replace 'YOUR_API_KEY' with your Firebase project's API key
        
        # Example response handling:
        if response.status_code == 200:
            print("Login successful:", response.json())
        else:
            print("Login failed:", response.json())

    def signup(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        # Similar to login(), send a request to Firebase Authentication endpoint for sign-up
        # Example request:
        response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=my_api_key', data={'email': email, 'password': password, 'returnSecureToken': True})

    def forgot_password(self, instance):
        email = self.email_input.text
        # Similar to login() and signup(), send a request to Firebase Authentication endpoint for password reset
        # Example request:
        response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=my_api_key', data={'email': email, 'requestType': 'PASSWORD_RESET'})


if __name__ == '__main__':
    MyApp().run()
