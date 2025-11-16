from kivy.uix.button import Button

def create_close_btn():
    return Button(
                text="Close",
                background_normal="",
                background_color=(0.85, 0.1, 0.1, 1),
                color=(1, 1, 1, 1),
                size_hint=(0.5, 0.1),
            )