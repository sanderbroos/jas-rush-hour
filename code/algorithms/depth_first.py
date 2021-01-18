import copy
from code.util import *
from queue import LifoQueue

class DepthFirst():
    """
    A Depth First algorithm that builds a stack of games each with cars in an unique position
    """
    def __init__(self, game):
        self.game = copy.deepcopy(game)
        self.states = LifoQueue()
        self.best_solution = None
        self.best_value = float('inf')
        
        # the maximum number of moves to try
        self.depth = 22
        self.archive = [self.game.board.get_board()]
    
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

        previous_move = game.previous_move()

        for move in moves:
            new_game = copy.deepcopy(game)
            # don't move the same car in consecutive moves
            if move[0] == previous_move[0]:
                continue
            
            new_game.move(move[0], move[1])
            new_board = new_game.board.get_board()
            
            if new_board not in self.archive:
                self.states.put(new_game)
                self.archive.append(new_board)

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
            
            if len(new_game.get_moves()) < self.depth and not new_game.won():
                xcol = new_game.cars.get('X').col
                if xcol:
                    print(f"depth: {len(new_game.get_moves())}        i = {i}      X at {xcol}         archive size: {len(self.archive)}      {self.states.__class__.__name__} size: {self.states.qsize()}")
                
                self.build_children(new_game)
            elif new_game.won():
                if self.__class__.__name__ == "BreadthFirst":
                    break
                elif self.__class__.__name__ == "DepthFirst":
                    self.check_solution(new_game)

        # update the input game with the best result found.
        self.game = self.best_solution
        if self.game:
            self.game.output()