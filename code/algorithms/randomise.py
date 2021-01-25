from random import choice
from code.util import all_moves, clean_moves, random_move_quick
from numpy import mean, std
from copy import deepcopy

class RandomOnce():
    def __init__(self, game, max_moves=float('inf'), fastest=False):
        self.game = deepcopy(game)

        # abort algorithm if the amount of moves exceeds this value
        self.max_moves = max_moves
        self.fastest = fastest


    def run(self):
        """ 
        Continues to selects a random move from all_moves untill the game is won
        """
        while not self.game.won():
            if self.fastest:
                move = random_move_quick(self.game)
            else:
                move = choice(all_moves(self.game))

            self.game.move(move[0], move[1])

            if len(self.game.get_moves()) > self.max_moves:
                return []
        
        return self.game.get_moves()
        


class Random():
    """ 
    Benchmarks the random algorithm by repeating the same algortihm for a select amount
    """

    def __init__(self, game, repeats=None, fastest=False):
        self.game = game
        self.numb_moves = []
        self.best_value = float('inf')
        self.best_moves = []
        self.repeats = repeats

        # if True, look for the fastest solution by aborting when # of moves exceeds best solution
        self.fastest = fastest
    

    def run(self):
        if not self.repeats:
            self.repeats = int(input("How many times should the randomise algorithm be executed? "))
            print()
        
        for i in range(self.repeats):
            algorithm = RandomOnce(self.game, max_moves=(self.best_value if self.fastest else float('inf')), self.fastest)
            moves_made = clean_moves(algorithm.run())
            
            if moves_made:
                print(f"{i + 1}: {len(moves_made)} moves made")
                self.numb_moves.append(len(moves_made))

                if len(moves_made) < self.best_value:
                    self.best_moves = moves_made
                    self.best_value = len(moves_made)
        
        if self.repeats > 1 and not self.fastest:
            print(f"\nmean: {int(mean(self.numb_moves))}\n"
                    f"std:  {int(std(self.numb_moves))}\n"
                    f"min:  {min(self.numb_moves)}\n"
                    f"max:  {max(self.numb_moves)}")

        return self.best_moves