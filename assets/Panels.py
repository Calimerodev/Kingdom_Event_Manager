from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.behaviors.touchripple import Color
from kivy.uix.actionbar import Label
from kivy.uix.image import Image
from kivy.uix.actionbar import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.graphics import Color , Rectangle
from kivy.uix.scrollview import ScrollView

#class for lateral Panels------------------------------------------------------------------->
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
#------------------------------------------------------------------------------------------>
#
#
#Class for create Navegation Bar----------------------------------------------------------->
class NavBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
#------------------------------------------------------------------------------------------>
#
#
#class for center panel-------------------------------------------------------------------->   
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
#------------------------------------------------------------------------------------------>
#
#
#Table------------------------------------------------------------------------------------->
class RowTable(GridLayout):
    def __init__(self, data , background = (0.2,0.2,0.2,1) , hover_color=(0.4,0.4,0.4, 1), **kwargs):
        super().__init__(**kwargs)
        self.cols = len(data)
        self.size_hint_y = None
        self.height = 40
        self.background = background
        self.hover_color = hover_color

        #init Background
        with self.canvas.before:
            Color(*self. background)
            self.rect = Rectangle(size = self.size , pos = self.pos)
        self.bind(size=self._update_rect , pos = self._update_rect)

        #init Cells
        for d in data:
            self.add_widget(Label(text = d , color=(1,1,1,1)))

        #Move Detect
        Window.bind(mouse_pos=self.on_mouse_pos)


    def _update_rect(self , *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    
    def on_mouse_pos(self , window, pos):
        if self.collide_point(*self.to_widget(*pos)):
            self._set_color(self.hover_color)
        else:
            self._set_color(self.background)


    def _set_color(self , color):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(size = self.size , pos = self.pos)



class Table(GridLayout):
    def __init__(self , header = [] , rows = [] , **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 2
        self.padding = 5


        Theader = RowTable(
                        header,
                        background=(0.1,0.1,0.1,1),
                        hover_color=(0.2,0.2,0.2,1)
                    )
        self.add_widget(Theader)

        cols = rows

        for i,row in enumerate(cols):
            background = (0.2,0.2,0.2,1) if i%2==0 else (0.25,0.25,0.25,1)
            hover = (0.4,0.4,0.4,1)
            self.add_widget(RowTable(
                                row,
                                background=background,
                                hover_color=hover
                            ))
#------------------------------------------------------------------------------------------>
