from queue import PriorityQueue
from code.heuristics import null_heuristic, block_heuristic, double_block_heuristic
from code.algorithms.breadth_first import BreadthFirst
import textwrap


class Astar(BreadthFirst):
    """
    Astar algorithm class inherits from Breadthfirst class
    """
    def __init__(self, game):
        super().__init__(game)
        self.states = PriorityQueue()
        self.heuristics = {
            'NULL': [null_heuristic, "No heuristic (BreathFirst)"],
            'BL': [block_heuristic, "Blocking cars"],
            '2BL': [double_block_heuristic, "Double blocking cars"]
        }
        self.heuristic = None
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
        priority = self.set_priority(self.game)
        depth = len(moves)
        self.counter += 1
        return self.states.put((priority, depth, self.counter, moves))
   

    def dequeue(self):
        """
        Get the next state from the Priority queue.
        """
        return self.states.get()[3]


    def run(self):
        """
        Ask the user to choose a heuristic, and then execute the algorithm.
        """

        print("Available heuristics:")
        for key, value in self.heuristics.items():
            print(f"    {key:>2}: {value[1]}")
        
        heuristic = 'None'
        while heuristic not in self.heuristics:
            heuristic = input(f"""Which heuristic do you want to use? Possiblities are: {', '.join(self.heuristics)}. """).upper()

        self.heuristic = self.heuristics[heuristic][0]

        return super().run()