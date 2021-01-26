import copy
from code.util import *
from queue import LifoQueue
from .breadth_first import BreadthFirst

class DepthFirst(BreadthFirst):
    """
    A Depth First algorithm that builds a stack of games each with cars
    in an unique position
    """
    def __init__(self, game):
        super().__init__(game)
        self.states = LifoQueue()
        self.depth = 22
        
  
    def check_solution(self):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = len(self.game.get_moves())
        
        # looking for solutions with the least amount of moves
        if new_value < self.best_value:
            self.best_solution = copy.deepcopy(self.game)
            self.best_value = new_value
            print(f"New best value: {self.best_value}")