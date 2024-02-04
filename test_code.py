from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
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
         #for email input field
        self.email_input = TextInput(
            multiline=False,
            hint_text='Enter Email',
            padding_y=(10, 0),
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.email_input)
        
        
        # for password_input field

        self.password_input = TextInput(
            multiline=False,
            password=True,
            hint_text='Enter Password',
            padding_y=(10, 0),
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.password_input)

        self.add_widget(Button(
            text='Forgot Password',
            on_press=self.forgot_password
        ))

        self.add_widget(Button(
            text='Login',
            on_press=self.login
        ))

        self.add_widget(BoxLayout(
            orientation='horizontal',
            padding=(0, 10, 0, 0),
            spacing=5,
            size_hint=(1, None),
            height=40
        ))
        self.ids['signup_button'] = Button(
            text='Sign up',
            font_size=20,
            on_press=self.signup
        )
        self.add_widget(self.ids['signup_button'])

    def login(self ):
        email = self.email_input.text
        password = self.password_input.text
        print(f'email: {email}')
        print(f'Password: {password}')

        # Make a request to your server for authentication
        response = requests.post("http://your-server/login", json={"username": username, "password": password})

        # Handle the server's response
        if response.status_code == 200:
            print("Login successful!")
        else:
            print("Login failed:", response.text)        
        
    def forgot_password(self ):
        
        pass

    def signup(self, ):
        
        pass

if __name__ == '__main__':
    MyApp().run()
