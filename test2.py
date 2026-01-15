from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

class BotonCircular(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (40, 40)  # más pequeño
        self.background_normal = ""
        self.background_color = (0, 0, 0, 0)  # transparente

        with self.canvas.before:
            # Fondo azul
            Color(0.1, 0.4, 0.9, 1)
            self.circle = Ellipse(size=self.size, pos=self.pos)

            # Borde blanco (usamos otro nombre)
            Color(1, 1, 1, 1)
            self.border_line = Line(circle=(self.center_x, self.center_y, self.width/2), width=2)

        # Actualizar cuando cambie tamaño o posición
        self.bind(pos=self._update_graphics, size=self._update_graphics)

    def _update_graphics(self, *args):
        # Actualizar círculo
        self.circle.pos = self.pos
        self.circle.size = self.size
        # Actualizar borde
        self.border_line.circle = (self.center_x, self.center_y, self.width/2)

class MiApp(App):
    def build(self):
        return BotonCircular(text="X", color=(1,1,1,1))  # texto blanco

if __name__ == "__main__":
    MiApp().run()
