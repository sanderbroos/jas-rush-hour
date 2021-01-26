from code.util import all_moves
from queue import Queue
from copy import deepcopy
from time import time


class BreadthFirst():
    """
    A Breadth First algorithm that builds a queue of games each with cars in an unique position.
    """
    def __init__(self, game):
        self.game = deepcopy(game)
        self.states = Queue()
        self.best_solution = None   
        self.best_value = float('inf')     
        self.archive = set()

        # needed for depth first search
        self.depth = float('inf')
        

    def enqueue(self, moves):
        """
        Add the given moves to the queue.
        """
        return self.states.put(moves)


    def dequeue(self):
        """
        Take the item at the front of the queue.
        """
        return self.states.get()


    def check_archive(self):
        """
        Add board to archive if it is new.
        """
        str_board = str(self.game.board)

        if str_board not in self.archive:
            self.archive.add(str_board)
            return True

        return False


    def build_children(self):
        """
        Creates all child states and adds them to queue.
        """
        # save the current moves before building children
        original_moves = deepcopy(self.game.get_moves())

        # execute all possible moves for this board
        for move in all_moves(self.game):
            new_moves = original_moves + [move]
            
            # build a game with this new list of moves
            self.game.reset()
            self.game.build(new_moves)
            
            # only enqueue if the generated board is new
            if self.check_archive():
                self.enqueue(new_moves)


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
        """
        Returns whether the current game is a winning solution.
        """
        return self.game.won()


    def run(self):
        """
        Runs the algorithm until all possible states are visited.
        """
        # show how long the algorithm takes while running it
        self.start = time()

        # add the current moves as first item in the queue
        self.enqueue(self.game.get_moves())
        
        # if a depth wasn't given, ask the user for it
        if not self.depth:
            self.depth = int(input("What's the maximum depth to search? "))
            print()
        
        iterations = 0
        
        while not self.states.empty():
            # build a game with the first element in the queue
            self.game.build(self.dequeue())
            
            # keep building children until max depth is reached or game is won
            if len(self.game.get_moves()) < self.depth and not self.win():
                self.build_children()
            elif self.win():
                self.check_solution()
                self.print_status(iterations)

                # depth first will keep looking until the queue is empty
                if self.__class__.__name__ == "BreadthFirst" or self.__class__.__name__ == "modAstar":
                    break

            # print a status update to show the progress
            iterations += 1
            if iterations % 100 == 0:
                self.print_status(iterations)
                
            self.game.reset()

        # if the whole queue was finished and still no solution found
        if not self.best_solution:
            print("\nFailed to find a solution.\n")
            return False
        
        # update the input game with the best result found.
        return self.best_solution.get_moves()
    
    def print_status(self, iterations):
        """
        Prints a status update to show the progress of the algorithm.
        """
        print(f"depth: {len(self.game.get_moves()):<12} iterations: {iterations:<12} archive size: {len(self.archive):<12} {self.states.__class__.__name__} size: {self.states.qsize():<12} time elapsed: {time() - self.start:.1f} s", end="\r")