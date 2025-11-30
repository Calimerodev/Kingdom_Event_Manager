import kivy
from kivy.core import text
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from assets.Panels import *
from kivy.app import App

class Test(App):
    def build(self):
        
        self.root = FloatLayout()
        
        map = Image(source="assets/imgs/village_1.jpg") 
        self.root.add_widget(map)
        
        centerpanel = CenterPanel(
                        pos = (70 , 70),
                        size_hint=(0.3 , 0.3)
                    )
        self.root.add_widget(centerpanel)

        return self.root


Test().run()
