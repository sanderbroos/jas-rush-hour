from code.util import *
from code.heuristics import *
from .depth_first import DepthFirst
from queue import Queue
import copy



class BreadthFirst(DepthFirst):
    """
    A Breadth First algorithm that builds a queue of games each with cars in an unique position
    """
    def __init__(self, game):
        super().__init__(game)
        self.states = Queue()
        self.depth = float('inf')

    def TEST_best_moves(self, game, heuristic):
        """
        returns list with 'best moves' using a heuristic

        heurtics variable moet zorgen dat je uit meerdere heurtics kan kiezen
        nu is block heurtics gehardcoded
        """
        moves = all_moves(game)
        best_moves = []
        # some surely bigger number (for block!!)
        best_heur = game.size


        for move in moves:
            new_game = copy.deepcopy(game)
            new_game.move(move[0], move[1]) 
            new_heur = block_heuristic(new_game)

            if new_heur == best_heur:
                best_moves.append(move)
            elif new_heur < best_heur:
                best_heur = new_heur
                best_moves = []
                best_moves.append(move)
            else:
                continue

        return best_moves
            
            
            









