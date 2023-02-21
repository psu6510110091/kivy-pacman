from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class Player(Widget):
    pac_img = StringProperty('images/pac_right.gif')

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
  
    def move(self):
        print('moving')
        self.pos = Vector(*self.velocity)+self.pos
        
        if self.velocity == [0, 1]:
            self.pac_img = "images/pacUp.gif"
        elif self.velocity == [0, -1]:
            self.pac_img = "images/pacDown.gif"
        elif self.velocity == [-1, 0]:
            self.pac_img = "images/pacLeft.gif"
        elif self.velocity == [1, 0]:
            self.pac_img = "images/pacRight.gif"
        