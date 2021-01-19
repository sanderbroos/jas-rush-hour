import copy
from code.util import *
from queue import Queue
from code.classes.board import Board

class BreadthFirstv1():

    def __init__(self, game):
        self.cars = copy.deepcopy(game.cars)
        self.size = game.size
        self.queue = Queue()
        self.archive = set()
        self.depth = 0
    
    def dequeue(self):
        """
        Choose next state of the game
        """
        return self.queue.get()

    def enqueue(self, item):
        self.queue.put(item)


    def get_childern(self,cars):
        """
        Creates all child states and add to a list
        """
        # board is used to get all_moves
        board = Board(self.size, cars)
        board = board.board
        moves = all_movesv1(cars,board)

        for car in moves:
            new_cars = copy.deepcopy(cars)

            if car[0].orientation == 'H':
                car[0].col = car[0].col + car[1]
            
            if car[0].orientation == 'V':
                car[0].row = car[0].row + car[1]
        
            self.enqueue(new_cars)

    def won(self,cars):

        carX = cars.get('X')

        if carX.col == self.size - 2:
            return True

        return False

    def run(self):

        # start node in queue
        self.queue.put(copy.deepcopy(self.cars))
        i = 0

        while not self.queue.empty():

            new_cars = self.dequeue()
            i += 1

            if not self.won(new_cars):
                xcol = new_cars.get('X').col
                if xcol:
                    print(f"depth: {self.depth}        i = {i}      X at {xcol}         archive size: {len(self.archive)}    queue size: {self.queue.qsize()}")
                self.get_childern(new_cars)
            