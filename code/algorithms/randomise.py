import random
from code.util import *
from code.classes.game import *
import itertools
import numpy as np

def random_car(cars):
    return random.choice(list(cars.values()))

def random_move(car, board):
    possibilities = get_possiblities(car, board)
    if not possibilities:
        return None

    return random.choice(possibilities)


def random_benchmark(repeats):
     
    numb_moves = []

    for _ in itertools.repeat(None,repeats):

        game = Game(6, "data/Rushhour6x6_3.csv")

        while not game.won():
            car = random_car(game.cars)
            move = random_move(car, game.board)
            game.move(car.name, move)

        numb_moves.append(len(game.moves))
    
    return (f"mean: {int(np.mean(numb_moves))}\n"
            f"std:  {int(np.std(numb_moves))}\n"
            f"min:  {min(numb_moves)}\n"
            f"max:  {max(numb_moves)}")

         