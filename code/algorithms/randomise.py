import random
from code.util import *

def random_car(cars):
    car = random.choice(list(cars.values()))
    
    return car

def random_move(car, board):
    possibilities = get_possiblities(car, board)
    if not possibilities:
        return None

    move = random.choice(possibilities)
    return move




