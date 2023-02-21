from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector

bpoint = {}
bpoint[1] = (89,40)
bpoint[2] = (1032,40)
bpoint[3] = (89,283)
bpoint[4] = (1032,283)

bpoint[5] = (255,40)
bpoint[6] = (255,283)

bpoint[7] = (510,40)
bpoint[8] = (510,283)

bpoint[9] = (688,40)
bpoint[10] = (688,40)

bpoint[11] = (866,40)
bpoint[12] = (866,283)

bpoint[13] = (178,121)
bpoint[14] = (255,121)
bpoint[15] = (178,202)
bpoint[16] = (255,202)

bpoint[17] = (510,121)
bpoint[18] = (599,121)
bpoint[19] = (599,202)
bpoint[20] = (688,202)

bpoint[21] = (955,121)
bpoint[22] = (1032,121)
bpoint[23] = (955,202)
bpoint[24] = (1032,202)

bpoint[25] = (777,40)
bpoint[26] = (777,121)

bpoint[27] = (0,159)
bpoint[28] = (89,159)
bpoint[29] = (1032,159)
bpoint[30] = (1109,159)

class Player(Widget):
    pac_img = StringProperty('images/pacRight.gif')

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
        