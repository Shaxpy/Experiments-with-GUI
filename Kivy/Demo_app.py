
# import os 
# os.environ['KIVY_IMAGE'] = 'pil,sdl2'
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter #make objects big and small
from kivy.uix.gridlayout import GridLayout #size of device
from kivy.uix.textinput import TextInput
class grid(GridLayout):
    def __init__(self,**kwargs):
        super(grid,self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text="Name="))
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)

#Inheritance

class TestApp(App):
    def build(self):
       return grid()

if __name__ == "__main__":
    TestApp().run()
