import copy
from code.util import *
from queue import Queue, PriorityQueue
from code.classes.board import Board
from code.heuristics import *
from code.algorithms.breadth_first import BreadthFirst

class Astar(BreadthFirst):

    def __init__(self, game, heuristic = 'NULL'):
        super().__init__(game)
        self.states = PriorityQueue()
        self.heuristics = {
            'NULL' : null_heuristic,
            'BL' : block_heuristic,
            '2BL' : double_block_heuristic
        }
        self.heuristic = self.heuristics[heuristic]


    def set_priority(self, game):
        return self.heuristic(game)


    def enqueue(self, move):
        priority = self.set_priority(self.game)
        print(priority, move)
        return self.states.put((priority, move))

   
    def dequeue(self):
        return self.states.get()[1]
