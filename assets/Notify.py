from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.app import App

class ToastNotification(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (300, 50)
        self.pos = (Window.width/2 - 150, Window.height - 100)
        self.halign = 'center'
        self.valign = 'middle'
        self.color = (1, 1, 1, 1)  # Blanco
        self.bold = True
        self.font_size = 16
        
        # Fondo rojo para errores
        with self.canvas.before:
            Color(0.8, 0.2, 0.2, 0.9)  # Rojo semitransparente
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def show(self, message, duration=3):
        """Muestra el mensaje por 'duration' segundos"""
        self.text = message
        self.opacity = 0
        
        # Animación de entrada
        anim_in = Animation(opacity=1, duration=0.3)
        anim_in.start(self)
        
        # Programar salida
        Clock.schedule_once(lambda dt: self.hide(), duration)
    
    def hide(self):
        """Oculta el mensaje con animación"""
        anim_out = Animation(opacity=0, duration=0.5)
        anim_out.bind(on_complete=lambda *args: self.parent.remove_widget(self))
        anim_out.start(self)

# Clase para gestionar múltiples notificaciones
class NotificationManager:
    def __init__(self, root_widget):
        self.root = root_widget
        self.notifications = []
    
    def show_error(self, message, duration=3):
        """Muestra un mensaje de error"""
        toast = ToastNotification()
        self.root.add_widget(toast)
        toast.show(message, duration)
        self.notifications.append(toast)
        
        # Mover notificaciones anteriores hacia abajo
        for i, notif in enumerate(self.notifications[:-1]):
            target_y = Window.height - 100 - (i + 1) * 60
            Animation(y=target_y, duration=0.3).start(notif)
        
        # Limpiar lista después de que desaparezcan
        Clock.schedule_once(lambda dt: self.cleanup(toast), duration + 0.5)
    
    def cleanup(self, toast):
        if toast in self.notifications:
            self.notifications.remove(toast)

