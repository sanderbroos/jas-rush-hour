import csv
from .car import Car
from code.util import get_lane, get_possiblities
from ..util import *


"""
-1/+1 bij het inladen van de cars te veranderen naar array style om code beter
leesbaar te houden. Input object wel naam bij move. CarX weggehaald, Welke output lijst bij moves.append? 
tried playing game, moves bug out at the bottom right corner
"""

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
                cars[row['car']] = Car(row['car'], row['orientation'], int(row['col']) - 1, int(row['row']) - 1, int(row['length']))

        return cars
    
    def create_board(self):
        # initialize empty 2D list representation of board
        # car objects in array
        board = [[None for i in range(self.size)] for j in range(self.size)]

        for car in self.cars.values():
            for i in range(car.length):
                if car.orientation == 'H':
                    board[car.row][car.col + i] = car
                if car.orientation == 'V':
                    board[car.row + i][car.col] = car

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
    

    def move(self, car, direction):
        # move trucks or cars, check is validmove etc the save new place in car class, save moves made for output file
        # and save the moves in self.moves
        moved_car = self.cars.get(car)

        if self.is_valid_move(moved_car, direction) is False:
            return False

        if moved_car.orientation == 'H':
            moved_car.col = moved_car.col + direction

            for i in range(moved_car.length):
                self.board[moved_car.row][moved_car.col - direction + i] = None

            for i in range(moved_car.length):
                self.board[moved_car.row][moved_car.col + i] = moved_car
                
                            
        if moved_car.orientation == 'V':
            moved_car.row = moved_car.row + direction

            for i in range(moved_car.length):
                self.board[moved_car.row - direction + i][moved_car.col] = None

            for i in range(moved_car.length):
                self.board[moved_car.row + i][moved_car.col] = moved_car

        # need to append the car name and direction to moves to save for output
        self.moves.append(f'{car}, {direction}')
        self.moves.append([moved_car.name, direction])
        return True


    def is_valid_move(self, car, move):
        # conditions for valid move: if car horizontal move needs to be horizontal, vertical car vertical move,
        # space to be moved to needs to be empty, If border game move cant pass it.

        moves = get_possiblities(car, self.board, self.size)

        if move in moves:
            return True
            
        return False
    


    def won(self):
        """
        Game is won if the path to the exit is cleared for car X.
        If won, move the car to the exit.
        """
        
        car_x = self.cars.get('X')


        # snap dit neit [car_x.col + 1:]):

        # if any spot in the path to the exit is occupied, the game is not won
        if any(get_lane(car_x, self.board)[car_x.col + 1:]):
            return False

        # otherwise the path is free, so move the car to the exit
        self.move(car_x.name, self.size - car_x.col - 1)
        return True


    def output(self):
        # maak van lijst moves een csv-achtig iets. need to clear list after game is won?
        pass
        