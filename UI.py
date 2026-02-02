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
from kingdom import *
from lighthouse import *
from utils import * 

class ScreenVillages(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        self.root = FloatLayout()

        btn_change_screen_main = Button(text="Back")
        btn_change_screen_main.bind(on_press=self.change_screen_main)
        self.root.add_widget(btn_change_screen_main)

        self.add_widget(self.root)


    def change_screen_main(self, instance):
        self.manager.transtion = SlideTransition(direction="right" , duration=0.3)
        self.manager.current = "screen_main"



class EventManagerApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(ScreenMain(name="screen_main"))
        sm.add_widget(ScreenVillages(name="screen_villages"))
        sm.add_widget(ScreenTest(name="test"))
        sm.add_widget(ScreenKingdom(name="screen_kingdom"))
        sm.add_widget(ScreenLightHouseVillage(name="screen_lighthouse_village"))
        return sm
