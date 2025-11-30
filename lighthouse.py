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
from utils import *
from models.data_filter import *
from models.models import *

class ScreenLightHouseVillage(Screen):
    cursor_x = NumericProperty(0)
    cursor_y = NumericProperty(0)
    def __init__(self, **kw):
        super().__init__(**kw)
        self.root = FloatLayout()
        map = Image(source="assets/imgs/lighthouse.png")
        self.root.add_widget(map) 

        btn_back = Button(
            text="Back",
            size_hint = (None , None),
            pos = (0,0),
            on_press=self.change_screen_main
        )
        
        self.root.add_widget(btn_back)
        
        

        
        
        #self.add_widget()
        
        #Test Position ------------------------------------------------------------------>
        self.test_csr_position = Label(
                    text="Cursor Position",
                    size_hint = (0 , 0)
                )
        self.root.add_widget(self.test_csr_position)
        #-------------------------------------------------------------------------------->
        

        #Panels Show Events-------------------------------------------------------------->
        self.show_events_panel = CenterPanel(
                                    pos = (70,70),
                                    size_hint = (0.7, 0.7)
                                )

        events = Manager_Events().filter("lighthouse")

        for e in events:
            self.show_events_panel.add_widget(Label(text=e[1]))
        
        self.root.add_widget(self.show_events_panel)
        #--------------------------------------------------------------------------------> 

        self.add_widget(self.root)


    def change_screen_main(self, instance):
        self.manager.transition = SlideTransition(direction="left", duration=0.3)
        self.manager.current = "screen_main"
    

    def on_touch_move(self, touch):
        self.cursor_x , self.cursor_y = touch.x , touch.y
        self.test_csr_position.pos = (touch.x , touch.y)
        self.test_csr_position.text = f"x:{self.cursor_y} , y:{self.cursor_y}"
