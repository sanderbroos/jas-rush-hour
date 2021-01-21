import random
from code.util import *
from code.classes.game import *
import itertools
import numpy as np
import copy


class Random():
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

        # do we want this in run, gets looped by benchmark? in main better?
        # self.game.output()
        # self.game.draw_board()
        print(f"{len(self.game.get_moves())} moves made")


class BenchmarkRandom:
    """ Benchmarks the random algorithm
    using choose car first then move method"""

    def __init__(self, game):
        self.game = game
        self.numb_moves = []
        self.best_value = float('inf')
        self.best_moves = []
    
    def run(self):
        repeats = int(input("How many times should the randomise algorithm be executed? "))
        
        for _ in itertools.repeat(None, repeats):
            algorithm = Random(self.game)
            algorithm.run()
            moves_made = algorithm.game.get_moves()
            self.numb_moves.append(len(moves_made))

            if len(moves_made) < self.best_value:
                self.best_moves = moves_made
                self.best_value = len(moves_made)
                algorithm.game.output()
        
        print(f"\nmean: {int(np.mean(self.numb_moves))}\n"
                f"std:  {int(np.std(self.numb_moves))}\n"
                f"min:  {min(self.numb_moves)}\n"
                f"max:  {max(self.numb_moves)}")