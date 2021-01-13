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

def all_random_moves(game):
    
    moves = []
    for car in game.cars.keys():
        possibilities = get_possiblities(game.cars.get(car), game.board)

        for move in possibilities:
            moves.append([car, move])
    
    return random.choice(moves)


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
            f"max:  {max(numb_moves)}",
            numb_moves)
    


def random_benchmarkv1(repeats):
     
    numb_moves = []

    for _ in itertools.repeat(None,repeats):

        game = Game(6, "data/Rushhour6x6_3.csv")

        while not game.won():
            moves = all_random_moves(game)
            car = moves[0]
            move = moves[1]
            game.move(car, move)

        numb_moves.append(len(game.moves))
    
    return (f"mean: {int(np.mean(numb_moves))}\n"
            f"std:  {int(np.std(numb_moves))}\n"
            f"min:  {min(numb_moves)}\n"
            f"max:  {max(numb_moves)}")