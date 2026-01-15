from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class Demo(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Botón inicial
        self.boton = Button(text="Subo y bajo", size_hint=(.2, .1), pos=(200, 200))
        self.add_widget(self.boton)

        # Iniciar animación infinita
        self.animar()

    def animar(self):
        # Animación hacia arriba
        anim_up = Animation(y=400, duration=1)
        # Animación hacia abajo
        anim_down = Animation(y=200, duration=1)

        # Encadenar animaciones
        anim = anim_up + anim_down

        # Al terminar, repetir
        anim.bind(on_complete=lambda *args: self.animar())
        anim.start(self.boton)

class DemoApp(App):
    def build(self):
        return Demo()

DemoApp().run()

