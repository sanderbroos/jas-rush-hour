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

class RandomOnce():
    def __init__(self,game):
        self.game = copy.deepcopy(game)
        

    def run(self):
        """ 
        Continues to selects a random move from all_moves untill the game is won
        """
        while not self.game.won():
            move = random.choice(all_moves(self.game))
            self.game.move(move[0], move[1])
  
        print(f"{len(self.game.get_moves())} moves made")


class Random:
    """ 
    Benchmarks the random algorithm by repeating the same algortihm for a select amount
    """

    def __init__(self, game):
        self.game = game
        self.numb_moves = []
        self.best_value = float('inf')
        self.best_moves = []
    
    def run(self):
        repeats = int(input("How many times should the randomise algorithm be executed? "))
        print()
        
        for _ in itertools.repeat(None, repeats):
            algorithm = RandomOnce(self.game)
            algorithm.run()
            moves_made = algorithm.game.get_moves()
            self.numb_moves.append(len(moves_made))

            if len(moves_made) < self.best_value:
                self.best_moves = moves_made
                self.best_value = len(moves_made)
                algorithm.game.output()
        
        if repeats > 1:
            print(f"\nmean: {int(np.mean(self.numb_moves))}\n"
                    f"std:  {int(np.std(self.numb_moves))}\n"
                    f"min:  {min(self.numb_moves)}\n"
                    f"max:  {max(self.numb_moves)}")