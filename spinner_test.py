from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        self.label = Label(text="Selecciona un elemento")

        spinner = Spinner(
            text="Opción 1",                # Texto inicial
            values=("Opción 1", "Opción 2", "Opción 3"),  # Lista de opciones
            size_hint=(None, None),
            size=(150, 44)
        )

        # Evento cuando cambia la selección
        spinner.bind(text=self.on_select)

        root.add_widget(spinner)
        root.add_widget(self.label)
        return root

    def on_select(self, spinner, text):
        self.label.text = f"Seleccionaste: {text}"

MyApp().run()

