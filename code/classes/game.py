import csv
from .car import Car
from ..util import *

class Game:

    def __init__ (self, size, source_file):
        self.size = size

        # load board and everything on it
        self.cars = self.load_cars(source_file)
        self.board = self.create_board()
        self.moves = []
        
    def load_cars(self, source_file):
        # load dictionary with key name car and value the car 
        cars = {}
        with open(source_file, 'r') as readfile:
            reader = csv.DictReader(readfile)

            for row in reader:
                if row['car'] == 'X':
                    carX = True
                else:
                    carX = False
                cars[row['car']] = Car(row['car'], row['orientation'], int(row['col']), int(row['row']), int(row['length']), carX)

        return cars
    
    def create_board(self):
        # initialize empty 2D list representation of board
        # car objects in array 
        board = [[None for i in range(self.size)] for j in range(self.size)]

        for car in self.cars.values():
            for i in range(car.length):
                if car.orientation == 'H':
                    board[car.row - 1][car.col - 1 + i] = car
                if car.orientation == 'V':
                    board[car.row - 1 + i][car.col - 1] = car

        return board
        
    def draw_board(self):
        # draw board and everthing on it
        to_draw = self.board

        for row in to_draw:
            for item in row:
                if item is None:
                    print('_', end=' ')
                else:
                    print(item.name, end=' ')
            print('')
    
    def move(self, direction):
        # move trucks or cars, check is validmove etc the save new place in car class, save moves made for output file
        # and save the moves in self.moves
        pass


    def is_valid_move(self, car, coordinate, move):
        # conditions for valid move: if car horizontal move needs to be horizontal, vertical car vertical move,
        # space to be moved to needs to be empty, If border game move cant pass it.
        
        pass


    def won(self):
        """
        Game is won if the path to the exit is cleared for car X.
        If won, move the car to the exit.
        """
        
        car_x = self.cars.get('X')

        # if any spot in the path to the exit is occupied, the game is not won
        if any(get_lane(car_x, self.board)[car_x.col + 1:]):
            return False

        # otherwise the path is free, so move the car to the exit
        self.move(car_x, self.size - car_x.col - 1)
        return True


    def output(self):
        # maak van lijst moves een csv-achtig iets.
        pass
        