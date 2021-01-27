from queue import PriorityQueue
from code.heuristics import null_heuristic, block_heuristic, double_block_heuristic
from code.algorithms.breadth_first import BreadthFirst


class Astar(BreadthFirst):
    """
    Astar algorithm class inherits from Breadthfirst class.
    """
    def __init__(self, game, heuristic = 'NULL'):
        super().__init__(game)
        self.states = PriorityQueue()
        self.heuristics = {
            'NULL': null_heuristic,
            'BL': block_heuristic,
            '2BL': double_block_heuristic,}
        self.heuristic = self.heuristics[heuristic]
        self.counter = 0


    def set_priority(self, game):
        """
        Use the current heuristic to determine the 
        heuristic value of the given game.
        """
        return self.heuristic(game)


    def enqueue(self, moves):
        """
        Priority order: heuristic value, depth, counter.
        """
        heuristic_value = self.set_priority(self.game)
        depth = len(moves)
        self.counter += 1

        return self.states.put((heuristic_value, depth, self.counter, moves))
   

    def dequeue(self):
        """
        Get the next state from the Priority queue.
        """
        return self.states.get()[3]
