from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # ScrollView que contendrá la tabla
        scroll = ScrollView(size_hint=(1, None), size=(400, 300))

        # Tabla con GridLayout
        table = GridLayout(cols=3, size_hint_y=None)
        table.bind(minimum_height=table.setter('height'))  # Ajusta la altura según el contenido

        # Rellenar la tabla con datos
        for i in range(50):  # muchas filas para que aparezca el scroll
            table.add_widget(Label(text=f"Fila {i+1} - Col 1", size_hint_y=None, height=40))
            table.add_widget(Label(text=f"Fila {i+1} - Col 2", size_hint_y=None, height=40))
            table.add_widget(Label(text=f"Fila {i+1} - Col 3", size_hint_y=None, height=40))

        scroll.add_widget(table)
        root.add_widget(scroll)

        return root

MyApp().run()

