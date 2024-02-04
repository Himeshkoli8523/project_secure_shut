import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        
        self.top_grid.add_widget(Label(text="Username: "))
        self.username_input = TextInput(multiline=False,height = 50,
                             width = 150,size_hint_y = None,
                             size_hint_x = None)
        self.top_grid.add_widget(self.username_input)
        
        self.top_grid.add_widget(Label(text="Password: "))
        self.password_input = TextInput(multiline=False, password=True)
        self.top_grid.add_widget(self.password_input)
        
         # Add top_grid to the main GridLayout
         
        self.add_widget(self.top_grid) 
        # signup button
        self.signup = Button(text = "sign up",
                             font_size = 32,
                             size_hint_y = None,
                             size_hint_x = None,
                             height = 50,
                             width = 150
                             
                             )
        self.add_widget(self.signup)

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()
