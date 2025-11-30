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
from utils import *

class ScreenTest(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        B = BoxLayout()

        B.add_widget(Label(text="Test"))

        allresources = get_resources()
        cnt = 0
        for resource in allresources:
            l = Label(
                text=resource[1],
                pos_hint= {"x":0 , "y":0}    
            )
            B.add_widget(l)

        self.add_widget(B)

