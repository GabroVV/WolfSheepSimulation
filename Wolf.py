import math


class Wolf(object):
    def __init__(self, speed, sheep_list):
        self.coordinates = [0.0, 0.0]
        self.wolf_move_dist = speed
        self.sheep_list = sheep_list

    def distance(self, sheep):
        difference_x = self.coordinates[0] - sheep.coordinates[0]
        difference_x *= difference_x
        difference_y = self.coordinates[1] - sheep.coordinates[1]
        difference_y *= difference_y
        distance = math.sqrt(difference_y + difference_x)
        return distance

    def find_closest_sheep(self):
        min_distance = self.distance(self.sheep_list[0])
        for i in range(len(self.sheep_list)):
            dist = self.distance(self.sheep_list[i])
            if dist < min_distance:
                min_distance = dist
        return min_distance




