from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage

class SecureShutApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.show_login_screen()
        return self.root

    def show_login_screen(self):
        login_layout = BoxLayout(orientation='vertical', spacing=10, padding=[10, 0, 10, 10])

        # Header Section
        header = BoxLayout(orientation='vertical', spacing=5)
        header.add_widget(Label(text='Welcome\nTo\nSecureShut', font_size='24sp', halign='center'))
        header.add_widget(Label(text='Enter Email', font_size='14sp'))

        email_input = TextInput(hint_text='Email', multiline=False)

        header.add_widget(Label(text='Password', font_size='14sp'))
        password_input = TextInput(hint_text='Password', password=True, multiline=False)

        forget_password_label = Label(text='Forget Password?', font_size='12sp', halign='right')

        login_button = Button(text='Login', on_press=self.show_registration_screen)

        login_layout.add_widget(header)
        login_layout.add_widget(email_input)
        login_layout.add_widget(password_input)
        login_layout.add_widget(forget_password_label)
        login_layout.add_widget(login_button)

        self.root.clear_widgets()
        self.root.add_widget(login_layout)

    def show_registration_screen(self, instance):
        registration_layout = BoxLayout(orientation='vertical', spacing=10, padding=[10, 0, 10, 10])

        # Header Section
        header = BoxLayout(orientation='vertical', spacing=5)
        header.add_widget(Label(text='Welcome\nTo\nSecureShut', font_size='24sp', halign='center'))
        header.add_widget(Label(text='Enter Email', font_size='14sp'))
        email_input = TextInput(hint_text='Email', multiline=False)
        header.add_widget(Label(text='Re Enter Email', font_size='14sp'))
        re_enter_email_input = TextInput(hint_text='Re Enter Email', multiline=False)
        header.add_widget(Label(text='Password', font_size='14sp'))
        password_input = TextInput(hint_text='Password', password=True, multiline=False)

        forget_password_label = Label(text='Forget Password?', font_size='12sp', halign='right')

        sign_up_button = Button(text='Sign up', on_press=self.show_login_screen)

        registration_layout.add_widget(header)
        registration_layout.add_widget(email_input)
        registration_layout.add_widget(re_enter_email_input)
        registration_layout.add_widget(password_input)
        registration_layout.add_widget(forget_password_label)
        registration_layout.add_widget(sign_up_button)

        self.root.clear_widgets()
        self.root.add_widget(registration_layout)

if __name__ == '__main__':
    SecureShutApp().run()
