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


    def build_children(self):
        """
        Creates all child states and add to a list
        """

        original_moves = copy.deepcopy(self.game.get_moves())
        previous_move = self.game.previous_move()

        for move in all_moves(self.game):
            # don't move the same car in consecutive moves
            if move[0] == previous_move[0]:
                continue
                
            # new_moves = original_moves + [move]
            
            # self.game.reset()
            # self.game.build(new_moves)
            # new_board = copy.deepcopy(self.game.board.get_board())
            
            # if new_board not in self.archive:
            self.states.put(original_moves + [move])
                # self.archive.append(new_board)


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


    def TEST_best_moves(self, game, heuristic):
        """
        returns list with 'best moves' using a heuristic

        heurtics variable moet zorgen dat je uit meerdere heurtics kan kiezen
        nu is block heurtics gehardcoded
        """
        moves = all_moves(game)
        best_moves = []
        # some surely bigger number (for block!!)
        best_heur = game.size

        for move in moves:
            new_game = copy.deepcopy(game)
            new_game.move(move[0], move[1]) 
            new_heur = block_heuristic(new_game)

            if new_heur == best_heur:
                best_moves.append(move)
            elif new_heur < best_heur:
                best_heur = new_heur
                best_moves = []
                best_moves.append(move)
            else:
                continue

        return best_moves


    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        self.states.put(self.game.get_moves())
        i = 0

        while self.states:
            new_state = self.get_next_state()
            self.game.build(new_state)

            i += 1
            
            if len(self.game.get_moves()) < self.depth and not self.game.won():
                if i%100==0:
                    print(f"depth: {len(self.game.get_moves())}        i = {i}      X at {self.game.cars['X'].col}         archive size: {len(self.archive)}      {self.states.__class__.__name__} size: {self.states.qsize()}")
                
                self.build_children()
            elif self.game.won():
                if self.__class__.__name__ == "BreadthFirst":
                    break
                elif self.__class__.__name__ == "DepthFirst":
                    self.check_solution(self.game)

            self.game.reset()

        # update the input game with the best result found.
        self.game = self.best_solution
        if self.game:
            self.game.output()