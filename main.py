from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

Window.size = (1200,400)

class GamePlay(Screen):
    ps = NumericProperty(77)
    ww = NumericProperty(1200)
    wh = NumericProperty(400)

class Wall(Widget):
    pass

class PacmanApp(App):
    def build(self):
        return GamePlay()

PacmanApp().run()