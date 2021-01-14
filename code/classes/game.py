import csv
from .car import Car
from ..util import *


class Game:
    """
    Class which facilitates the playability of the game
    """
    def __init__ (self, size, source_file):
        self.size = size

        # load board and everything on it
        self.cars = self.load_cars(source_file)
        self.board = self.create_board()
        self.moves = []

        # self.possible_moves = all_moves(self.cars, self.board)
        

    def load_cars(self, source_file):
        """
        Loads dictionary with the name of the car as key and the car as value 
        """

        cars = {}
        with open(source_file, 'r') as readfile:
            reader = csv.DictReader(readfile)

            for row in reader:
                cars[row['car']] = Car(row['car'], row['orientation'], int(row['col']) - 1, int(row['row']) - 1, int(row['length']))

        return cars
    

    def create_board(self):
        """
        Initialize empty 2D list representation of board and adds the car objects
        """

        board = [[None for i in range(self.size)] for j in range(self.size)]

        for car in self.cars.values():
            for i in range(car.length):
                if car.orientation == 'H':
                    board[car.row][car.col + i] = car
                if car.orientation == 'V':
                    board[car.row + i][car.col] = car

        return board
        

    # def get_next_move(self):
    #     if self.possible_moves:
    #         return self.possible_moves.pop()
        
    #     return None


    def draw_board(self):
        """
        Draws board and everthing on it
        """

        to_draw = self.board

        for row in to_draw:
            for item in row:
                if item == None:
                    print('_', end=' ')
                else:
                    print(item.name, end=' ')
            print('')
    

    def move(self, car, direction):
        """
        If the move is vaild, moves the car and saves the move
        """

        moved_car = self.cars.get(car)

        if not self.is_valid_move(moved_car, direction):
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

        self.moves.append([car, direction])
        return True


    def is_valid_move(self, car, move):
        """
        Checks for validity of the to be played move
        """

        return move in get_possiblities(car, self.board)
    

    def won(self):
        """
        Returns true when the game is won, if no cars are blocking the exit
        """
        
        car_x = self.cars.get('X')

        # if any spot in the path to the exit is occupied, the game is not won
        if any(get_lane(car_x, self.board)[car_x.col + car_x.length:]):
            return False

        # otherwise the path is free, so move the car to the exit
        self.move(car_x.name, self.size - car_x.col - car_x.length)

        self.moves = clean_moves(self.moves)

        return True


    def output(self):
        """
        Cleans and saves the made moves to an output file
        """
        self.moves = clean_moves(self.moves)

        output_string = "car,move"
        for move in self.moves:
            if move[1] != 0:
                output_string += f'\n{move[0]},{move[1]}'

        f = open("output.csv", "w")
        f.write(output_string)
        f.close()