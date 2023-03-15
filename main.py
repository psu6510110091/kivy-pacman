from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.core.window import Window
from player import *
from ghost import *
from food import *
from kivy.clock import Clock
from kivy.uix.label import Label

Window.size =(1200,400)
    
class GamePlay(Screen):
    ps = NumericProperty(77)
    ww = NumericProperty(1200)
    wh = NumericProperty(400)

    ghost1 = Ghost()
    ghost2 = Ghost()
    pacman = Player()

    food_point = ['point{0}'.format(i) for i in range(0, len(food))]

    game_progress = 'on'
    def __init__(self, **kwargs):
        super(GamePlay,self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'up':
            self.pacman.velocity=(0,1)
        elif keycode[1] == 'down':
            self.pacman.velocity=(0,-1)
        elif keycode[1] == 'left':
            self.pacman.velocity=(-1,0)
        elif keycode[1] == 'right':
            self.pacman.velocity=(1,0)
        return True

    def show_food(self):
        for i in range(0, len(food)):
            if i != 179 and 1 != 170:
                globals()[self.food_point[i]] = Points(pos=food[i], size = (5,5))
                self.add_widget(globals()[self.food_point[i]])

    def update(self, dt):
        if self.game_progress == 'on':
            self.pacman.move()
            if self.powerball.collide_player(self.pacman):
                self.remove_widget(self.powerball)
                self.pacman.powerup = 1

            for i in reversed(range(len(eaten))):
                if (self.pacman.pos[0] <= food[eaten[i]][0] - 20) and (
                    self.pacman.pos[0] >= food[eaten[i]][0] - 50) \
                    and (self.pacman.pos[1] <= food[eaten[i]][1] - 20) and (
                        self.pacman.pos[1] >= food[eaten[i]][1] - 50):
                    self.remove_widget(globals()['point{0}'.format(eaten[i])])
                    del eaten[i]
                    self.pacman.score += 1

            for gost in [self.ghost1, self.ghost2]:
                if self.pacman.powerup == 0:
                    if distance(self.pacman.pos,gost.pos) <= 77/2:
                        self.remove_widget(self.pacman)
                        self.game_progress = 'Lost'
                
                else :
                    if distance(self.pacman.pos,gost.pos) <= 77/2:
                        self.remove_widget(gost)
                        gost.pos = [0,0]
                        del gost
                        self.pacman.powerup = 0        
                        self.pacman.score += 200

    def update_ghost1(self,dt):
        self.ghost1.strategy()

    def do_strategy(self,dt):
        self.ghost1.next_strategy(self.pacman.close_point)

    def update_ghost2(self,dt):
        self.ghost2.strategy()

    def do_strategy2(self,dt):
        self.ghost2.next_strategy2(self.pacman.close_point)    
                
class Wall(Widget):
    pass

class PacmanApp(App):
    def build(self):
        game = GamePlay() 
        game.show_food()
        def start_delay(self):
            Clock.schedule_interval(game.update_ghost2, 1.0 / 60.0)
        Clock.schedule_once(start_delay,5)
        Clock.schedule_interval(game.do_strategy2, 10)
        Clock.schedule_interval(game.update_ghost1, 1.0 / 60.0)
        Clock.schedule_interval(game.do_strategy, 5)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

PacmanApp().run()