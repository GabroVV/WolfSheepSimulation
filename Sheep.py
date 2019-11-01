import random as rd


class Sheep(object):
    def __init__(self, speed, limit):
        x = rd.random() * limit
        y = rd.random() * limit
        self.coordinates = [x, y]
        self.sheep_move_dist = speed
