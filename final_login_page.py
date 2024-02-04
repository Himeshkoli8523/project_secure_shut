from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import keys
import requests


class MyApp(App):

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
        
        try:
            user = self.firebase.authentication.sign_in_with_password(email,password)
            print(f"Successfully logged in: {user}")
        except Exception as e :
            print(f"Login failed : {e}")
            
        

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
