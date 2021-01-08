import csv

from .car import Car


class Board:

    def __init__ (self, size, source_file):
        self.size = size

        # load board and everything on it
        self.cars = self.load_cars(source_file)
        self.board = self.create_board()
        
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
        board = [['_' for i in range(self.size)] for j in range(self.size)]

        for car in self.cars.values():
            for i in range(car.length):
                if car.orientation == 'H':
                    board[car.row - 1][car.col - 1 + i] = car.name
                if car.orientation == 'V':
                    board[car.row - 1 + i][car.col - 1] = car.name

        return board
        
    def draw_board(self):
        # draw board and everthing on it
        to_draw = self.board

        for row in to_draw:
            for item in row:
                print(f'{item} ', end='')
            print('')
    
    def move(self, direction):
        # move trucks or cars, check is validmove etc the save new place in car class, save moves made for output file
        
        pass

    def won(self):
        # game won, car in space just before gate means game is won
        pass
    
    def is_valid_move(self):
        # conditions for valid move: if car horizontal move needs to be horizontal, vertical car vertical move,
        # space to be moved to needs to be empty, If border game move cant pass it.
        pass
