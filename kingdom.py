from kivy.uix.accordion import NumericProperty
from kivy.uix.filechooser import Screen
from kivy.uix.behaviors.touchripple import Color
from kivy.uix.actionbar import Label
from kivy.uix.image import Image
from kivy.uix.actionbar import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.graphics import Color , Rectangle
from assets.Panels import *
from assets.buttons.btns import *
from kivy.uix.screenmanager import Screen , ScreenManager , SlideTransition
from kivy.uix.widget import Widget
from main import * 
from screentest import *
from utils import *


class ScreenKingdom(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.root = FloatLayout()
        map = Image(source="assets/imgs/Kingdom_map.jpg")
        self.root.add_widget(map)
        btn_back = Button(
                    text="Back",
                    size_hint=(None,None),
                    pos=(0,0),
                    on_press=self.change_screen_main
                )
        
        self.root.add_widget(btn_back)
        self.add_widget(self.root)
        
        
    def change_screen_main(self , instance):
        self.manager.transition = SlideTransition(direction="left" , duration=0.3)
        self.manager.current = "screen_main"

