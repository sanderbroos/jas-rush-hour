from code.util import *
from code.heuristics import *
from queue import Queue
import copy



class BreadthFirst():
    """
    A Breadth First algorithm that builds a queue of games each with cars in an unique position
    """

    def __init__(self, game):
        self.game = copy.deepcopy(game)
        self.states = Queue()
        self.best_solution = None   
        self.best_value = float('inf')     
        self.archive = set()
        self.depth = float('inf')
        

    def get_next_state(self):
        """
        Choose next state of the game
        """
        return self.states.get()


    def build_children(self):
        """
        Creates all child states and add to a list
        """

        original_moves = copy.deepcopy(self.game.get_moves())

        for move in all_moves(self.game):
            new_moves = original_moves + [move]
            
            self.game.reset()
            self.game.build(new_moves)
            str_board = str(self.game.board)
            
            if str_board not in self.archive:
                self.states.put(new_moves)
                self.archive.add(str_board)
            
        self.game.reset()
        self.game.build(original_moves)

    def check_solution(self):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = len(self.game.get_moves())
        
        # looking for solutions with the least amount of moves
        if new_value < self.best_value:
            self.best_solution = copy.deepcopy(self.game)
            self.best_value = new_value
            print(f"New best value: {self.best_value}")

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        self.states.put(self.game.get_moves())
        i = 0

        while not self.states.empty():
            new_state = self.get_next_state()
            self.game.build(new_state)

            i += 1
            
            if len(self.game.get_moves()) < self.depth and not self.game.won():
                if i%100==0:
                    self.print_status(i)

                self.build_children()
                
            elif self.game.won():
                self.print_status(i)
                self.game.draw_board()
                self.check_solution()
                if self.__class__.__name__ == "BreadthFirst":
                    break

            self.game.reset()

        # update the input game with the best result found.
        if self.best_solution:
            self.best_solution.output()
        else:
            print("\nFailed to find a solution.")

    
    def print_status(self, i):
        print(f"depth: {len(self.game.get_moves()):<12} i = {i:<12} X at {self.game.cars['X'].col:<10} archive size: {len(self.archive):<12} {self.states.__class__.__name__} size: {self.states.qsize()}")