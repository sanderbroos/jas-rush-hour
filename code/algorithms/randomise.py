import random
from code.util import *
from code.classes.game import *
import itertools
import numpy as np
import copy


class RandomAlgoritm():
    def __init__(self,game):
        self.game = copy.deepcopy(game)


    def get_car(self):
        """ Randomly chooses a car"""
        return random.choice(list(self.game.cars.values()))


    def get_move(self,car):
        """ Randomly chooses a move for a given car """
        possibilities = get_possiblities(car, self.game.board.get_board())

        if not possibilities:
            return None

        return random.choice(possibilities)


    def all_moves(self):
        """Randomly chooses a move from all possible moves for all cars """
    
        moves = []
        for car in self.game.cars.keys():
            possibilities = get_possiblities(self.game.cars.get(car), self.game.board.get_board())

            for move in possibilities:
                moves.append([car, move])

        return random.choice(moves)


    def run(self):
        """ Chooses a car then a move and returns the number
        of moves needed to win the game """
        while not self.game.won():
            car = self.get_car()
            move = self.get_move(car)
            self.game.move(car.name, move)

        return len(self.game.moves)


def Benchmark_random(game, repeats):
    """ Benchmarks the random algorithm
    using choose car first then move method"""

    numb_moves = []

    for _ in itertools.repeat(None,repeats):
        algorithm = RandomAlgoritm(game)
        numb_moves.append(algorithm.run())
    
    return (f"mean: {int(np.mean(numb_moves))}\n"
            f"std:  {int(np.std(numb_moves))}\n"
            f"min:  {min(numb_moves)}\n"
            f"max:  {max(numb_moves)}",
            numb_moves)


def random_car(cars):
    return random.choice(list(cars.values()))


def random_move(car, board):
    possibilities = get_possiblities(car, board.get_board())
    if not possibilities:
        return None

    return random.choice(possibilities)


def all_random_moves(game):
    moves = []
    for car in game.cars.keys():
        possibilities = get_possiblities(game.cars.get(car), game.board.get_board())

        for move in possibilities:
            moves.append([car, move])
    
    return random.choice(moves)


def random_benchmark(repeats):
    numb_moves = []

    for _ in itertools.repeat(None,repeats):

        game = Game(6, "data/Rushhour6x6_1.csv")

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