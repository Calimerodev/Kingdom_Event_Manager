from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class ScrollableTable(App):
    def build(self):
        # Configurar ScrollView
        scroll_view = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        
        # Crear GridLayout para la tabla (filas dinámicas)
        table_layout = GridLayout(
            cols=3,  # Número de columnas
            spacing=10,
            size_hint_y=None,  # Altura dinámica
            padding=20
        )
        table_layout.bind(minimum_height=table_layout.setter('height'))  # Ajustar altura
        
        # Agregar encabezados
        headers = ["Columna 1", "Columna 2", "Columna 3"]
        for header in headers:
            table_layout.add_widget(Label(text=header, bold=True, font_size=16))
        
        # Agregar datos de ejemplo (50 filas)
        for i in range(50):
            for col in range(3):
                table_layout.add_widget(Label(text=f"Dato {i+1}-{col+1}"))
        
        # Añadir GridLayout al ScrollView
        scroll_view.add_widget(table_layout)
        return scroll_view

if __name__ == "__main__":
    ScrollableTable().run()
