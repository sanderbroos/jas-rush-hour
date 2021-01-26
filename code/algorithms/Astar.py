from queue import PriorityQueue
from code.heuristics import null_heuristic, block_heuristic, double_block_heuristic
from code.algorithms.breadth_first import BreadthFirst


class Astar(BreadthFirst):
    """
    Astar algorithm class inherits from Breadthfirst class
    """
    def __init__(self, game, heuristic='None'):
        super().__init__(game)
        self.states = PriorityQueue()
        self.heuristics = {
            'NULL': null_heuristic,
            'BL': block_heuristic,
            '2BL': double_block_heuristic
        }
        self.heuristic_str = heuristic
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
        heuristics = {"NULL": "No heuristic (BreathFirst)",
                      "BL": "Blocking cars",
                      "2BL": "Double blocking cars"}

        print("Available heuristics:")
        for key, value in heuristics.items():
            print(f"    {key:>2}: {value}")
        
        while self.heuristic_str not in heuristics:
            self.heuristic_str = input(f"Which heuristic do you want to use? Possiblities are: {', '.join(heuristics)}. ").upper()

        self.heuristic = self.heuristics[self.heuristic_str]

        return super().run()