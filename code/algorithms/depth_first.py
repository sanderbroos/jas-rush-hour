import copy
from code.util import *
from queue import LifoQueue
from .breadth_first import BreadthFirst

class DepthFirst(BreadthFirst):
    """
    A Depth First algorithm that builds a stack of games each with cars in an unique position
    """
    def __init__(self, game, depth=None):
        super().__init__(game)
        self.states = LifoQueue()
        self.depth = depth
        self.archive = {}

    def build_children(self):
        """
        Creates all child states and add to a list
        """

        original_moves = copy.deepcopy(self.game.get_moves())

        for move in all_moves(self.game):
            new_moves = original_moves + [move]
            
            self.game.reset()
            self.game.build(new_moves)
            str_board = str(self.game.board)
            
            if str_board not in self.archive or len(new_moves) < self.archive[str_board]:
                self.states.put(new_moves)
                self.archive[str_board] = len(new_moves)
            
        self.game.reset()
        self.game.build(original_moves)