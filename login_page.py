from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.graphics import Color, Line

class SecureShutLoginApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', spacing=10, padding=[10, 0, 10, 10])

        # Header Section
        header = BoxLayout(orientation='vertical', spacing=5)
        header.add_widget(Label(text='Welcome\nTo\nSecureShut', font_size='24sp', halign='center',pos=(0,50)))
        header.add_widget(Label(text='Enter Email', font_size='12sp'))
        email_input = TextInput(multiline=False, hint_text='Email')
        header.add_widget(email_input)
        header.add_widget(Label(text='Password', font_size='12sp'))
        password_input = TextInput(multiline=False, password=True, hint_text='Password')
        header.add_widget(password_input)
        header.add_widget(Label(text='Forget Password?', font_size='12sp', halign='right', color=[1, 0.5, 0, 1]))
        root.add_widget(header)

        # Buttons Section
        buttons = BoxLayout(orientation='vertical', spacing=10)
        buttons.add_widget(Button(text='Login', background_color=[1, 0.5, 0, 1]))
        
        # Separator Lines
        separator_line = BoxLayout(size_hint_y=None, height=1)
        with separator_line.canvas:
            Color(1, 0.5, 0, 1)
            Line(points=[0, 0, separator_line.width, 0], width=1)
        buttons.add_widget(separator_line)

        buttons.add_widget(AsyncImage(source="https://cdn.builder.io/api/v1/image/assets/TEMP/"
                                             "b3c0e8c3d7344f9befe86fa6b471f7854a8baae1e820519bcd2531dde4162d7b?"
                                             "apiKey=30fe291997dd49fa803266d4fba39a6d&", size_hint_y=None, height=50))
        buttons.add_widget(Label(text="Don’t have an account?", font_size='12sp', halign='center'))
        buttons.add_widget(Button(text='Create new account', color=[1, 0.5, 0, 1], background_color=[0, 0, 0, 0]))
        root.add_widget(buttons)

        return root

if __name__ == '__main__':
    SecureShutLoginApp().run()
