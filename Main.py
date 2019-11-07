from Sheep import Sheep
from Wolf import Wolf
from Enums import Status
from FileOperations import FileOperations


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
        FileOperations.create_csv()

    def simulate(self):
        for i in range(0, self.sheep_count):
            self.sheep_list.append(Sheep(i, self.sheep_speed, self.limit))
        while self.turn <= self.turns and self.sheep_left_check():
            for sheep in self.sheep_list:
                sheep.update()
            self.wolf.update()
            self.display()
            FileOperations.append_to_csv([self.turn,self.count_alive_sheep()])
            self.turn += 1

    def count_alive_sheep(self):
        count = 0
        for sheep in self.sheep_list:
            if sheep.status == Status.Alive:
                count += 1
        return count

    def display(self):
        print("Turn number: ",end="")
        print(self.turn, end=" ")
        print("Wolf position: ")
        print(self.wolf.coordinates)
        print("Number of alive sheep:", end=' ')
        print(self.count_alive_sheep())
        print()

    def sheep_left_check(self):
        for sheep in self.sheep_list:
            if sheep.status == Status.Alive:
                return True
        return False


if __name__ == "__main__":
    sim = Simulation(50, 15, 0.5, 1.0, 10)
    sim.simulate()


