from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector

bpoint = {}
bpoint[1] = (89,40)
bpoint[2] = (1032,40)
bpoint[3] = (89,283)
bpoint[4] = (1032,283)

bpoint[5] = (0,159)
bpoint[6] = (89,159)
bpoint[7] = (1032,159)
bpoint[8] = (1109,159)

bpoint[9] = (255,40)
bpoint[10] = (255,283)

bpoint[11] = (688,40)
bpoint[12] = (688,283)

bpoint[13] = (866,40)
bpoint[14] = (866,283)

passages = []
passages = [bpoint[1] + bpoint[2], bpoint[2] + bpoint[4],bpoint[1] + bpoint[3],bpoint[3] + bpoint[4], \
            bpoint[5] + bpoint[6], bpoint[7] + bpoint[8], bpoint[9] + bpoint[10], bpoint[11] + bpoint[12], \
            bpoint[13] + bpoint[14]]

class Player(Widget):
    pac_img = StringProperty('images/pac_right.gif')

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    elan = (0,0)
    
    def move(self):

        last_pos = self.pos.copy()
        
        for passage in passages:
            if (passage[0] <= self.velocity_x + self.pos[0]) and \
               (passage[2] >= self.velocity_x + self.pos[0]) and \
               (passage[1] <= self.velocity_y + self.pos[1]) and \
               (passage[3] >= self.velocity_y + self.pos[1]):

                self.pos = Vector(*self.velocity)+self.pos
                self.elan = self.velocity.copy()
                
                if self.velocity == [0, 1]:
                    self.pac_img = "images/pac_up.png"
                elif self.velocity == [0, -1]:
                    self.pac_img = "images/pac_down.png"
                elif self.velocity == [-1, 0]:
                    self.pac_img = "images/pac_left.png"
                elif self.velocity == [1, 0]:
                    self.pac_img = "images/pac_right.png"

        if self.pos == last_pos:
            for passage in passages:
                if (passage[0] - 0.1 <= self.elan[0] + self.pos[0]) and \
                   (passage[2] + 0.1 >= self.elan[0] + self.pos[0]) and \
                   (passage[1] - 0.1 <= self.elan[1] + self.pos[1]) and \
                   (passage[3] + 0.1 >= self.elan[1] + self.pos[1]):
                    self.pos = Vector(*self.elan)+self.pos
