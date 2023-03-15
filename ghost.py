from kivy.uix.widget import Widget
from kivy.properties import StringProperty,NumericProperty,ReferenceListProperty
from kivy.vector import Vector
from random import randint
from math import *
from food import *
from player import passages, bpoint, graph, close_list
from Dijkstra import dijkstra, distance, armin

class Ghost(Widget):
    sp = StringProperty('images/ghost_1.png')

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(-1)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    elan = (0,-1)

    strat = (0,[])

    close_point = 26
    
    def move(self, randomly=True):

        last_pos = self.pos.copy()

        for passage in passages:
            if (passage[0] <= self.velocity_x + self.pos[0]) and \
               (passage[2] >= self.velocity_x + self.pos[0]) and \
               (passage[1] <= self.velocity_y + self.pos[1]) and \
               (passage[3] >= self.velocity_y + self.pos[1]):

                self.pos = Vector(*self.velocity)+self.pos
                self.elan = self.velocity.copy()
                
                if self.velocity == [-1, 0]:
                    self.sp = "images/ghost_1.png"

                if self.velocity == [1, 0]:
                    self.sp = "images/ghost_1.png"
                if self.velocity == [0, 1]:
                    self.sp = "images/ghost_1.png"
                if self.velocity == [0, -1]:
                    self.sp = "images/ghost_1.png"

        if self.pos == last_pos:
            for passage in passages:
                if (passage[0] - 0.1 <= self.elan[0] + self.pos[0]) and \
                   (passage[2] + 0.1 >= self.elan[0] + self.pos[0]) and \
                   (passage[1] - 0.1 <= self.elan[1] + self.pos[1]) and \
                   (passage[3] + 0.1 >= self.elan[1] + self.pos[1]):
                    self.pos = Vector(*self.elan)+self.pos

        if self.pos == [bpoint[27][0], (bpoint[27][1])]:
            self.pos = [bpoint[30][0], (bpoint[30][1])]

        elif self.pos == [bpoint[30][0], (bpoint[30][1])]:
            self.pos = [bpoint[27][0], (bpoint[27][1])]

        if self.pos == last_pos:
            if(self.strat[1]==[] or randomly) and ((self.pos[0], self.pos[1]) in bpoint):
               self.direction()
               self.move()

        self.close_point = \
            armin(lambda x:distance(self.pos, bpoint[x]),close_list[self.close_point -1], self.close_point)

    def direction(self):
        dep = randint(0,3)
        if dep == 0:
            self.velocity = (-1,0)
        if dep == 1:
            self.velocity = (1,0)
        if dep == 2:
            self.velocity = (0,1)
        if dep == 3:
            self.velocity = (0,-1)

    def strategy(self):
        try:
            if (self.pos[0], self.pos[1]) == bpoint[self.strat[1][0]]:
                self.strat = (self.strat[0], self.strat[1][1::])

            if (bpoint[self.strat[1][0]][1] - self.pos[1]) != 0:
                self.velocity = [0,(bpoint[self.strat[1][0]][1] - self.pos[1]) / abs(bpoint[self.strat[1][0]][1] - self.pos[1])]
            if (bpoint[self.strat[1][0]][0] - self.pos[0]) != 0:
                self.velocity = [(bpoint[self.strat[1][0]][0] - self.pos[0]) / abs(bpoint[self.strat[1][0]][0] - self.pos[0]), 0]
                
            self.move(False)
        except:
            self.move()

    def next_strategy(self, close_to_player):
        self.strat = dijkstra(self.close_point, close_to_player, graph)

    def next_strategy2(self, close_to_player):
        self.strat = dijkstra(self.close_point, close_to_player, graph)