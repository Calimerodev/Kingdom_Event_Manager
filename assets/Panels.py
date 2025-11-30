from kivy.uix.behaviors.touchripple import Color
from kivy.uix.actionbar import Label
from kivy.uix.image import Image
from kivy.uix.actionbar import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.graphics import Color , Rectangle

#class for lateral Panels
class LateralPanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Background Color
        with self.canvas.before:
            Color(0.15, 0.15, 0.15, 1)
            self.rect = Rectangle(size=self.size , pos=self.pos)
            
            self.bind(size=self._update_rect , pos=self._update_rect)

        
    def _update_rect(self , *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


#Class for create Navegation Bar
class NavBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

#class for center panel
class CenterPanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Background Color
        with self.canvas.before:
            Color(0.15, 0.15, 0.15, 0.6)
            self.rect = Rectangle(size=self.size , pos=self.pos)
            
            self.bind(size=self._update_rect , pos=self._update_rect)

        
    def _update_rect(self , *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
