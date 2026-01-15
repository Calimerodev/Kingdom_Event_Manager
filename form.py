import kivy
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class miApp(App):
    def build(self):
        b = BoxLayout()
        b.add_widget(TextInput())
        return b


miApp().run()
