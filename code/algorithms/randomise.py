import random
from code.util import *
from code.classes.game import *
import itertools
import numpy as np
import copy


class RandomAlgorithm():
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

        return len(self.game.get_moves())


    def Benchmark_random(self, game, repeats):
        """ Benchmarks the random algorithm
        using choose car first then move method"""

        numb_moves = []

        for _ in itertools.repeat(None,repeats):
            algorithm = RandomAlgorithm(game)
            numb_moves.append(algorithm.run())
        
        # output doesn't work like this
        self.game.output()
        self.game.draw_board()

        return (f"mean: {int(np.mean(numb_moves))}\n"
                f"std:  {int(np.std(numb_moves))}\n"
                f"min:  {min(numb_moves)}\n"
                f"max:  {max(numb_moves)}",
                numb_moves)