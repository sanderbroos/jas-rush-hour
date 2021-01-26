from queue import PriorityQueue
from code.heuristics import null_heuristic, block_heuristic, double_block_heuristic
from code.algorithms.breadth_first import BreadthFirst


class Astar(BreadthFirst):
    """
    Astar algorithm class inherits from Breadthfirst class
    """

    def __init__(self, game, heuristic = 'NULL'):
        super().__init__(game)
        self.states = PriorityQueue()
        self.heuristics = {
            'NULL' : null_heuristic,
            'BL' : block_heuristic,
            '2BL' : double_block_heuristic,
        }
        self.heuristic = self.heuristics[heuristic]
        self.counter = 0


    def set_priority(self, game):
        return self.heuristic(game)


    def enqueue(self, moves):
        """
        priority: heuristic value, depth, counter
        """
        depth = len(moves)
        priority = self.set_priority(self.game)
        self.counter += 1
        return self.states.put((priority, depth, self.counter, moves))
   
   
    def dequeue(self):
        
        # get value from priority tuple
        return self.states.get()[3]

