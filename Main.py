from Sheep import Sheep
from Wolf import Wolf

if __name__ == "__main__":
    sheep_list = {}
    for i in range(0,10):
        sheep_list[i] = Sheep(i, 0.5, 10)
        sheep_list[i].update()
    wolf = Wolf(1.0, sheep_list)
    print(wolf.find_closest_sheep())
