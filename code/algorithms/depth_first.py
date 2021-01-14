import copy
from code.util import *

class DepthFirst:
    """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, game):
        self.game = copy.deepcopy(game)
        self.states = [copy.deepcopy(self.game)]
        self.best_solution = None
        self.best_value = float('inf')

        # the maximum number of moves to try
        self.depth = 22
    
    def get_next_state(self):
        """
        Chose next state of the game
        """
        return self.states.pop()

    def build_children(self, game):
        """
        Creates all child states and add to a list
        """
        possibilities = all_moves(game)

        # adds a new possibile move to the stack of game states
        for value in possibilities:
            new_move = copy.deepcopy(game)

            if new_move.move(value[0], value[1]):
                self.states.append(new_move)

    def check_solution(self, new_game):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = len(new_game.moves)
        
        # looking for solutions with the least amount of moves
        if new_value < self.best_value:
            self.best_solution = new_game
            self.best_value = new_value
            print(f"New best value: {self.best_value}")

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        i = 0
        while self.states:            
            new_game = self.get_next_state()

            i += 1
            # print(i)
            
            if len(new_game.moves) < self.depth and not new_game.won():
                xcol = new_game.cars.get('X').col
                if xcol:
                    print(i, xcol)
                # retrieve the next car to move.
                # car = new_game.get_car()
                self.build_children(new_game)
            elif new_game.won():
                # stop if we find a solution
                # break

                # or continue looking for better game
                self.check_solution(new_game)

            # new_game.draw_board()

        # update the input game with the best result found.
        self.game = self.best_solution