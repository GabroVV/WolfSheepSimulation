from Sheep import Sheep
from Wolf import Wolf
from Enums import Status
from FileOperations import FileOperations
import argparse

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
        self.list_with_dictionaries = []
        self.dictionary = {}



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
            self.create_dictionary()
            FileOperations.append_dictionary_to_list(self.list_with_dictionaries,self.dictionary)

            self.turn += 1
        FileOperations.create_json(self.list_with_dictionaries)

    def count_alive_sheep(self):
        count = 0
        for sheep in self.sheep_list:
            if sheep.status == Status.Alive:
                count += 1
        return count

    def create_dictionary(self):
        self.dictionary["round_no"] = self.turn
        self.dictionary["wolf_pos"] = [self.wolf.coordinates[0],self.wolf.coordinates[1]]
        temp_list=[]
        for sheep in self.sheep_list:
            if sheep.status==Status.Alive:
                temp_list.append(sheep.coordinates)
            else:
                temp_list.append(None)
        self.dictionary["sheep_pos"] = temp_list

    def display(self):
        print("Turn number:", end="")
        print(self.turn)
        print("Wolf position:", end="")
        print(round(self.wolf.coordinates[0], 3), end ='')
        print(" , ", end='')
        print(round(self.wolf.coordinates[1], 3))
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


