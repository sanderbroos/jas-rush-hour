from queue import LifoQueue
from .breadth_first import BreadthFirst


class DepthFirst(BreadthFirst):
    """
    A Depth First algorithm that builds a stack of games each with cars in an unique position.
    """
    def __init__(self, game, depth=None):
        super().__init__(game)
        self.states = LifoQueue()
        self.depth = depth
        self.archive = {}


    def check_archive(self):
        """
        Add board to archive if it is new.
        """
        str_board = str(self.game.board)
        
        # save board to the archive if it's the least amount of moves for that board yet
        if len(self.game.get_moves()) < self.archive.get(str_board, float('inf')):
            self.archive[str_board] = len(self.game.get_moves())
            return True

        return False