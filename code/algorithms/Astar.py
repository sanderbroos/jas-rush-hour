from queue import PriorityQueue
from code.heuristics import null_heuristic, block_heuristic, double_block_heuristic
from code.algorithms.breadth_first import BreadthFirst


class Astar(BreadthFirst):
    def __init__(self, game, heuristic = 'None'):
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
        return self.heuristic(game)


    def enqueue(self, moves):
        """
        heur value first priority, depth second priority
        only problem no control over which object first if 
        same priority and depth 
        """
        depth = len(moves)
        priority = self.set_priority(self.game)
        self.counter += 1
        return self.states.put((priority, depth, self.counter, moves))
   

    def dequeue(self):
        return self.states.get()[3]


    def run(self):
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