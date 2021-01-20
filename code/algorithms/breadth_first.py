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