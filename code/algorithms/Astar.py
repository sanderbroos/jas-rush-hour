import copy
from code.util import *
from queue import Queue, PriorityQueue
from code.classes.board import Board

class Astar():

    def __init__(self, game):
        self.cars = copy.deepcopy(game.cars)
        self.size = game.size
        self.queue = PriorityQueue()
        self.archive = set()
    
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
