import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter #make objects big and small
from kivy.uix.gridlayout import GridLayout #size of device
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
        f=FloatLayout()
        s=Scatter()
        l=Label(text='Hello World',font_size=12)
        f.add_widget(s)
        s.add_widget(l)
        return f
TestApp().run()