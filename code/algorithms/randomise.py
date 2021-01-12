import random
from code.util import *

def random_car(cars):
    return random.choice(list(cars.values()))

def random_move(car, board):
    possibilities = get_possiblities(car, board)
    if not possibilities:
        return None

    return random.choice(possibilities)