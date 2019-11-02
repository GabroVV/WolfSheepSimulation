from Sheep import Sheep
from Wolf import Wolf
from Enums import Status

class Simulation(object):
    def __init__(self, turns, sheep_count, sheep_speed, wolf_speed, limit):
        self.turns = turns
        self.sheep_count = sheep_count
        self.sheep_speed = sheep_speed
        self.wolf_speed = wolf_speed
        self.limit = limit
        self.sheep_list = []
        self.wolf = Wolf(wolf_speed, self.sheep_list)
        self.turn = 1

    def simulate(self):
        for i in range(0, self.sheep_count):
            self.sheep_list.append(Sheep(i, self.sheep_speed, self.limit))
        while self.turn <= self.turns and self.sheep_left_check():
            for sheep in self.sheep_list:
                sheep.update()
            self.wolf.update()
            self.display()
            self.turn += 1

    def display(self):
        print("Turn number: ",end="")
        print(self.turn, end=" ")
        print("Wolf position: ")
        print(self.wolf.coordinates)
        print()

    def sheep_left_check(self):
        for sheep in self.sheep_list:
            if sheep.status == Status.Alive:
                return True
        return False


if __name__ == "__main__":
    sim = Simulation(50, 15, 0.5, 1.0, 10)
    sim.simulate()


