from threading import main_thread
from typing import clear_overloads
from kivy import _patch_mod_deps_win
from kivy.uix.textinput import TextInput 
from operator import add
from kivy.core import text
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
from kivy.uix.screenmanager import FallOutTransition, Screen , ScreenManager , SlideTransition
from kivy.uix.widget import Widget
from main import * 
from screentest import *
from kingdom import *
from utils import *
from models.data_filter import *
from models.models import *
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from assets import Notify

class ScreenLightHouseVillage(Screen):
    #global Atributes
    cursor_x = NumericProperty(0)
    cursor_y = NumericProperty(0)
    

    def __init__(self, **kw):
        super().__init__(**kw)
        self.root = FloatLayout()
        map = Image(source="assets/imgs/lighthouse.png")
        self.root.add_widget(map) 
        #Notification Manager
        self.notif_manager = Notify.NotificationManager(self.root)
        btn_back = Button(
            text="Back",
            size_hint = (None , None),
            pos = (0,0),
            on_press=self.change_screen_main
        )
        
        self.root.add_widget(btn_back)
         
        
        #self.add_widget()
        #
        #Test Position ------------------------------------------------------------------>
        self.test_csr_position = Label(
                    text="Cursor Position",
                    size_hint = (0 , 0)
                )
        self.root.add_widget(self.test_csr_position)
        #-------------------------------------------------------------------------------->
        #
        #Panels Show Events-------------------------------------------------------------->
        show_events_btn = Button(text = "show",
                                 on_press = self.show_center_pane_events,
                                 size_hint = (None , None),
                                 size = (200 , 100),
                                 pos = (100 , 0)
                            )
        self.root.add_widget(show_events_btn)
        self.show_events_panel = CenterPanel(
                                    pos_hint = {'x':0.150 , 'y':1},
                                    #pos_hint = {'x':0.150 , 'y':0.125},
                                    #pos = (300,150),
                                    size_hint = (0.7, 0.7)
                                )
        self.scroll_show_events = ScrollView(
                                size_hint=(1,1),
                                size=(self.show_events_panel.width, 
                                self.show_events_panel.height),
                                do_scroll_x = False,
                                do_scroll_y = True,
                                bar_color=[0.5, 0.5, 0.5, 0.8],
                                bar_inactive_color=[0.5, 0.5, 0.5, 0.2],
                                bar_width=12,
                                scroll_type=['bars', 'content'],
                                effect_cls='ScrollEffect',  # Efecto de scroll suave
                                always_overscroll = False    
                            )

        events = Manager_Events().filter("lighthouse")

        header = ['name' , 'start' , 'end' , 'action']

        event_tmp = []
        for e in events:
            del_btn = Button(
                            text='',
                            size_hint = (None , None),
                            size = (47 , 47),
                            border = (0,0,0,0),
                            #keep_ratio=False,
                            #allow_stretch=True,
                            valign="middle",
                            halign="left",
                            background_down = 'assets/buttons/delete_btn_down.png',
                            background_normal='assets/buttons/delete_btn.png', 
                            on_press=self.on_press_delete_events
                        )
            del_btn.id = e[0]
            tmp = (e[1] , e[5] , e[6] , del_btn)
            event_tmp.append(tmp)
        
        self.Table_Events = Table(header=header , rows=event_tmp , size_hint_y = None)
        self.Table_Events.bind(minimum_height = self.Table_Events.setter('height'))
        self.scroll_show_events.add_widget(self.Table_Events)
        self.show_events_panel.add_widget(self.scroll_show_events)
         
        
        self.root.add_widget(self.show_events_panel)

        Clock.schedule_once(self.focus_scroll_view , 0.2)

        #-------------------------------------------------------------------------------->
        #
        #Panel Add Events---------------------------------------------------------------->
        self.add_events_panel = CenterPanel(
                                    pos_hint = {"x":0.150 , "y":1},
                                    size_hint = (0.7 , 0.7)
                                )
        add_events_btn = Button(
                            text="add",
                            size_hint = (None , None),
                            size = (200 , 100),
                            pos = (300 , 0),
                            on_press = self.add_center_panel_events
                        )

        self.root.add_widget(add_events_btn)
    
        #form add events
        self.form_add_event = GridLayout()
        self.form_add_event.cols = 2
        self.form_add_event.padding = 20
        self.form_add_event.spacing = 15

        self.form_add_event.add_widget(Label(text = "Name Event"))
        self.name_event_form = TextInput(hint_text = "Type Event name" , multiline = False)
        self.form_add_event.add_widget(self.name_event_form)
        
        self.form_add_event.add_widget(Label(text = "Start"))
        self.start_event_form = TextInput(hint_text='select -> start')
        self.form_add_event.add_widget(self.start_event_form)
        
        self.form_add_event.add_widget(Label(text = "End"))
        self.end_event_form = TextInput(hint_text = 'select -> end' , multiline = False)
        self.form_add_event.add_widget(self.end_event_form)
        
        create_event_btn = Button(
                            text="Create",
                            on_press=self.create_event
                        )
        self.form_add_event.add_widget(create_event_btn)

        self.add_events_panel.add_widget(self.form_add_event)
        self.root.add_widget(self.add_events_panel)
        #-------------------------------------------------------------------------------->
        #
        self.add_widget(self.root)
#------------------------------------------------------------------------------------------
    
    
    def focus_scroll_view(self , dt):
        self.scroll_show_events.focus = True


    def on_press_delete_events(self , instance):
        Manager_Events().delete_event(instance.id)
        self.update_table()


    def update_table(self): 
        self.scroll_show_events.remove_widget(widget=self.Table_Events)
        events = Manager_Events().filter("lighthouse")

        header = ['name' , 'start' , 'end' , 'action']

        event_tmp = []
        for e in events:
            del_btn = Button(
                            text='',
                            size_hint = (None , None),
                            size = (47 , 47),
                            border = (0,0,0,0),
                            #keep_ratio=False,
                            #allow_stretch=True,
                            valign="middle",
                            halign="center",
                            background_down = 'assets/buttons/delete_btn_down.png',
                            background_normal='assets/buttons/delete_btn.png', 
                            on_press=self.on_press_delete_events
                        )
            del_btn.id = e[0] 
            tmp = (e[1] , e[5] , e[6] , del_btn)
            event_tmp.append(tmp)
        
        self.Table_Events = Table(header=header , rows=event_tmp , size_hint_y = None)
        self.Table_Events.bind(minimum_height = self.Table_Events.setter('height'))
        self.scroll_show_events.add_widget(self.Table_Events)
        Clock.schedule_once(self.focus_scroll_view , 0.2)



    #insert Event from form
    def create_event(self , instace):
        #Insert Event on Data Base if I Can
        if self.name_event_form.text == '' or self.start_event_form.text == '' or self.end_event_form.text == '':
            self.notif_manager.show_error('Error: Please fill in all fields')  
            return

        Manager_Events().insert_event(
                            self.name_event_form.text,
                            'lighthouse',
                            0,
                            -1,
                           
                            self.start_event_form.text,
                            self.end_event_form.text,
                            []
                        ) 
        #Reset Data
        self.name_event_form.text = ''
        self.end_event_form.text = ''
        self.start_event_form.text = ''
        #Update Table
        self.update_table()

    def add_center_panel_events(self , instance):
        anim = None
        if self.add_events_panel.pos_hint['y'] == 1:
            if self.show_events_panel.pos_hint['y'] != 1:
                anim2 = Animation(pos_hint = {'x':0.150 , 'y':1}, duration = 0.3)
                anim2.start(self.show_events_panel)
            anim = Animation(pos_hint = {'x':0.150 , 'y':0.125} , duration = 0.3)
        
        else:
            anim = Animation(pos_hint = {'x':0.150 , 'y':1} , duration = 0.3)
        
        anim.start(self.add_events_panel)


    def show_center_pane_events(self , instance):
        anim = None
        if self.show_events_panel.pos_hint['y'] == 1:
            if self.add_events_panel.pos_hint['y'] != 1:
                anim2 = Animation(pos_hint = {'x':0.150 , 'y':1} , duration = 0.3)
                anim2.start(self.add_events_panel)
            anim = Animation(pos_hint = {'x':0.150 , 'y':0.125} , duration = 0.3)
        else:
            anim = Animation(pos_hint = {'x':0.150 , 'y':1} , duration = 0.3)
        anim.start(self.show_events_panel)


    def change_screen_main(self, instance):
        self.manager.transition = SlideTransition(direction="left", duration=0.3)
        self.manager.current = "screen_main"
    

    def on_touch_move(self, touch):
        self.cursor_x , self.cursor_y = touch.x , touch.y
        self.test_csr_position.pos = (touch.x , touch.y)
        self.test_csr_position.text = f"x:{self.cursor_x} , y:{self.cursor_y}"
