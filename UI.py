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
from utils import *


class ScreenMain(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        root = FloatLayout()
        map = Image(
            source="assets/imgs/Region_map.jpeg",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0}
        )

        root.add_widget(map)

        #Navegation Bar
        nav_bar = BoxLayout(
            orientation="horizontal",
            size_hint=(1 , None),
            height=150,
            padding=5,
            spacing=5,
            pos_hint={"top": 1}
        )

        nav_bar_btns = {
            "Region":"assets/buttons/Region_Nav_bar.png",
            "Villages":"assets/buttons/Villages_Nav_bar.png",
            "Events":"assets/buttons/Events_Nav_bar.png",
            "Resources":"assets/buttons/Resources_Nav_bar.png",
        }

        for name , path in nav_bar_btns.items():
            x = None
            if name == "Region":
                x = lambda instance:self.procces_nav_bar_Region(instance , name = "Region")
            
            if name == "Villages":
                x = lambda instance:self.procces_nav_bar_Villages(instance , name = "Villages")
            
            if name == "Events":
                x = lambda instance:self.procces_nav_bar_Events(instance , name = "Events")
            
            if name == "Resources":
                x = lambda instance:self.procces_nav_bar_Resources(instance , name = "Resources")
            
            
            nav_bar_btn = Button(
                background_normal=path,
                size_hint=(None , None),
                size=(200 , 100),
                on_press = x
            )
            nav_bar.add_widget(nav_bar_btn)   

        root.add_widget(nav_bar)
        #End Navegation Bar

        #Events Panel
        self.panel_Events_manager = LateralPanel(
            orientation = "vertical",
            size_hint=(0.3 , 1),
            pos_hint={"x":1 , "y":0},
            padding=10,
            spacing=10
        )

        #Events Panel
        text_Events_panel = Label(text="Events(fase de prueba)")
        btn_panel_Events_close = create_close_btn()
        btn_panel_Events_close.bind(on_press=self.close_panel_Events)
        self.panel_Events_manager.add_widget(text_Events_panel)
        self.panel_Events_manager.add_widget(btn_panel_Events_close)
        
        #Region Panel
        #########################################################################>
        #Resources Panel
        self.panel_Resources_manager =  LateralPanel(
                                orientation = "vertical",
                                size_hint=(0.3 , 1),
                                pos_hint={"x":1 , "y":0},
                                padding=10,
                                spacing=10
                            )
        btn_panel_Resources_close = create_close_btn()
        btn_panel_Resources_close.bind(on_press=self.close_panel_Resources)
        text_Resources_panel = Label(text="Resources(fase de preuba)")
        self.panel_Resources_manager.add_widget(text_Resources_panel)
        self.panel_Resources_manager.add_widget(btn_panel_Resources_close)


        root.add_widget(self.panel_Resources_manager)
        root.add_widget(self.panel_Events_manager)

        btn_test = Button(
                        text="Test",
                        size_hint=(None , None),
                        size=(200 , 100),
                        on_press = x
                    )
        btn_test.bind(on_press=self.test_screen)

        root.add_widget(btn_test)

        self.add_widget(root)
    
    
    def test_screen(self , instance):
        self.manager.transition = SlideTransition(direction="right", duration=0.3)
        self.manager.current = "test"


    def procces_nav_bar_Region(self, instance , name=None):
        print(1)
    
    
    def procces_nav_bar_Villages(self, instance , name=None):
        self.manager.transition = SlideTransition(direction="left" , duration=0.3)
        self.manager.current = "screen_villages"
        print(1)

    
    def procces_nav_bar_Events(self, instance , name=None):
        anim = Animation(pos_hint={"x":0.7 , "y":0} , duration=0.3)
        anim.start(self.panel_Events_manager)
    
    
    def procces_nav_bar_Resources(self, instance , name=None):
        anim = Animation(pos_hint={"x":0.7,"y":0} , duration=0.3)
        anim.start(self.panel_Resources_manager)
    

    def close_panel_Events(self, instance):
        anim = Animation(pos_hint = {"x":1 ,"y": 0} , duration=0.3)
        anim.start(self.panel_Events_manager)


    def close_panel_Resources(self , instance):
        anim = Animation(pos_hint = {"x":1 ,"y": 0} , duration=0.3)
        anim.start(self.panel_Resources_manager)


#testeo no te metas eb dramas
class Screetest(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        B = FloatLayout()

        B.add_widget(Label(text="Test"))

        self.add_widget(B)
        

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

class miApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(ScreenMain(name="screen_main"))
        sm.add_widget(ScreenVillages(name="screen_villages"))
        sm.add_widget(Screetest(name="test"))

        return sm