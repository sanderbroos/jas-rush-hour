import random
from code.util import *
from code.classes.game import *
import itertools
import numpy as np
import copy

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
        
        return self.game.get_moves()
        


class Random():
    """ 
    Benchmarks the random algorithm by repeating the same algortihm for a select amount
    """

    def __init__(self, game, repeats=None):
        self.game = game
        self.numb_moves = []
        self.best_value = float('inf')
        self.best_moves = []
        self.repeats = repeats
    

    def run(self):
        if not self.repeats:
            self.repeats = int(input("How many times should the randomise algorithm be executed? "))
            print()
        
        for i in range(self.repeats):
            algorithm = RandomOnce(self.game)
            moves_made = clean_moves(algorithm.run())
            print(f"{i + 1}: {len(moves_made)} moves made")
            self.numb_moves.append(len(moves_made))

            if len(moves_made) < self.best_value:
                self.best_moves = moves_made
                self.best_value = len(moves_made)
                algorithm.game.output()
        
        if self.repeats > 1:
            print(f"\nmean: {int(np.mean(self.numb_moves))}\n"
                    f"std:  {int(np.std(self.numb_moves))}\n"
                    f"min:  {min(self.numb_moves)}\n"
                    f"max:  {max(self.numb_moves)}\n")

        return self.best_moves