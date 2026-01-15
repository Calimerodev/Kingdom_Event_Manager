from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Formulario(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.padding = 20
        self.spacing = 15

        # Campo Nombre
        self.add_widget(Label(text="Nombre:", font_size=18))
        self.nombre = TextInput(hint_text="Escribe tu nombre", multiline=False)
        self.add_widget(self.nombre)

        # Campo Email
        self.add_widget(Label(text="Email:", font_size=18))
        self.email = TextInput(hint_text="ejemplo@correo.com", multiline=False)
        self.add_widget(self.email)

        # Botón
        self.add_widget(Label())  # espacio vacío
        self.boton = Button(text="Enviar", background_color=(0.2, 0.6, 0.9, 1), on_press=self.f)
        self.add_widget(self.boton)

    
    def f(self , instance):
        print(self.nombre.text)
        self.nombre.text = ''        


class FormApp(App):
    def build(self):
        return Formulario()

FormApp().run()

