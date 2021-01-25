from code.util import all_moves
from queue import Queue
from copy import deepcopy
from time import time


class BreadthFirst():
    """
    A Breadth First algorithm that builds a queue of games each with cars in an unique position
    """

    def __init__(self, game):
        self.game = deepcopy(game)
        self.states = Queue()
        self.best_solution = None   
        self.best_value = float('inf')     
        self.archive = set()
        self.depth = float('inf')

        self.start = time()
        

    def enqueue(self, moves):
        return self.states.put(moves)


    def dequeue(self):
        return self.states.get()


    def build_children(self):
        """
        Creates all child states and add to a list
        """

        original_moves = deepcopy(self.game.get_moves())

        for move in all_moves(self.game):
            new_moves = original_moves + [move]
            
            self.game.reset()
            self.game.build(new_moves)
            str_board = str(self.game.board)
            
            if str_board not in self.archive:
                self.enqueue(new_moves)
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
            self.best_solution = deepcopy(self.game)
            self.best_value = new_value
            print()
            self.game.draw_board()
            print(f"Best solution: {self.best_value} moves\n")


    def win(self):
        return self.game.won()


    def run(self):
        """
        Runs the algorithm until all possible states are visited.
        """
        self.start = time()

        self.enqueue(self.game.get_moves())
        i = 0

        if not self.depth:
            self.depth = int(input("What's the maximum depth to search? "))
            print()

        while not self.states.empty():
            self.game.build(self.dequeue())

            i += 1
            if i%100==0:
                self.print_status(i)
            
            if len(self.game.get_moves()) < self.depth and not self.win():
                self.build_children()
            elif self.win():
                self.print_status(i)
                self.check_solution()
                if self.__class__.__name__ == "BreadthFirst" or self.__class__.__name__ == "modAstar":
                    break

            self.game.reset()

        # update the input game with the best result found.
        if self.best_solution:
            return self.best_solution.get_moves()

        print("\nFailed to find a solution.\n")
        return False

    
    def print_status(self, i):
        print(f"depth: {len(self.game.get_moves()):<12} i = {i:<12} X at {self.game.cars['X'].col:<10} archive size: {len(self.archive):<12} {self.states.__class__.__name__} size: {self.states.qsize():<12} time elapsed: {time() - self.start:.1f} s", end="\r")