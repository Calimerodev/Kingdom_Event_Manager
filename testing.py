from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class Fila(GridLayout):
    def __init__(self, datos, fondo=(0.2,0.2,0.2,1), hover_color=(0.4,0.4,0.4,1), **kwargs):
        super().__init__(**kwargs)
        self.cols = len(datos)
        self.size_hint_y = None
        self.height = 40
        self.fondo = fondo
        self.hover_color = hover_color

        # Fondo inicial
        with self.canvas.before:
            Color(*self.fondo)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Crear celdas (Labels)
        for dato in datos:
            self.add_widget(Label(text=dato, color=(1,1,1,1)))

        # Detectar movimiento del mouse
        Window.bind(mouse_pos=self.on_mouse_pos)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_mouse_pos(self, window, pos):
        if self.collide_point(*self.to_widget(*pos)):
            self._set_color(self.hover_color)
        else:
            self._set_color(self.fondo)

    def _set_color(self, color):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(size=self.size, pos=self.pos)

class Tabla(GridLayout):
    def __init__(self,a = 0, **kwargs):
        super().__init__(**kwargs)
        print(a)
        self.cols = 1
        self.spacing = 2
        self.padding = 5

        # Encabezados
        encabezado = Fila(["Nombre", "Edad", "Ciudad"], fondo=(0.1,0.1,0.1,1), hover_color=(0.2,0.2,0.2,1))
        self.add_widget(encabezado)

        # Filas de datos
        filas = [
            ("Ana", "23", "La Habana" , "12"),
            ("Carlos", "30", "Santiago" , "12"),
            ("Beatriz", "27", "Holguín" , "12"),
            ("Daniel", "35", "Camagüey" , "12"),
        ]

        for i, fila in enumerate(filas):
            fondo = (0.2,0.2,0.2,1) if i % 2 == 0 else (0.25,0.25,0.25,1)
            hover = (0.4,0.4,0.4,1)
            self.add_widget(Fila(fila, fondo=fondo, hover_color=hover))

class TablaApp(App):
    def build(self):
        return Tabla(a=1)

if __name__ == "__main__":
    TablaApp().run()
