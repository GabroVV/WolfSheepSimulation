import random as rd
from Enums import Directions
from Enums import Status


class Sheep(object):
    def __init__(self, index, speed, limit):
        x = rd.random() * limit
        y = rd.random() * limit
        self.index = index
        self.coordinates = [x, y]
        self.sheep_move_dist = speed
        self.status = Status.Alive

    def log(self):
        print("Sheep", end="")
        print(self.index, end=" ")
        print(Status(self.status).name, end=" ")
        print(self.coordinates)

    def update(self):
        if self.status == Status.Alive:
            direction = Directions.random_direction()
            if direction == Directions.North:
                self.coordinates[1] += self.sheep_move_dist
            elif direction == Directions.South:
                self.coordinates[1] -= self.sheep_move_dist
            elif direction == Directions.West:
                self.coordinates[0] -= self.sheep_move_dist
            elif direction == Directions.East:
                self.coordinates[0] += self.sheep_move_dist

    def die(self):
        self.status = Status.Dead
        print("Sheep", end="")
        print(self.index, end=" ")
        print("got eaten by wolf")





