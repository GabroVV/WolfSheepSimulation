import random as rd
from enum import Enum


class Directions(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

    @staticmethod
    def random_direction():
        return rd.choice([Directions.North, Directions.East, Directions.South, Directions.West])

class Status(Enum):
    Dead = 0
    Alive = 1


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
            print(direction)
            if direction == Directions.North:
                self.coordinates[1] += self.sheep_move_dist
            elif direction == Directions.South:
                self.coordinates[1] -= self.sheep_move_dist
            elif direction == Directions.West:
                self.coordinates[0] -= self.sheep_move_dist
            elif direction == Directions.East:
                self.coordinates[0] += self.sheep_move_dist






