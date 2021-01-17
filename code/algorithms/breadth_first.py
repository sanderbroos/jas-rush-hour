from code.util import *
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
        
    def get_next_state(self):
        """
        Choose next state of the game
        """
        return self.states.get()
    
    def build_children(self, game):
        """
        Creates all child states and add to a list
        """
        
        moves = all_moves(game)

        for move in moves:
            new_game = copy.deepcopy(game)

            if move[0] == move[0] and move[1] == -move[1]:
                continue
            
            new_game.move(move[0], move[1])
            self.states.put(new_game)


    def check_solution(self, new_game):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = len(new_game.get_moves())
        
        # looking for solutions with the least amount of moves
        if new_value < self.best_value:
            self.best_solution = new_game
            self.best_value = new_value
            print(f"New best value: {self.best_value}")


    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        self.states.put(copy.deepcopy(self.game))

        i = 0
        while self.states:         
            new_game = self.get_next_state()

            i += 1
          
            if not new_game.won():
                xcol = new_game.cars.get('X').col
                print(f"depth: {len(new_game.get_moves())}        i = {i}      X at {xcol}    queue size: {self.states.qsize()}")
                
                self.build_children(new_game)
            elif new_game.won():
                # stop if we find a solution
                # break

                # or continue looking for better game
                self.check_solution(new_game)
                break

        # update the input game with the best result found.
        self.game = self.best_solution
            