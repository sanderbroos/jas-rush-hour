import csv
from .board import Board
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
        self.board = Board(self.size, self.cars)
        self.moves = []

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


    def draw_board(self):
        """
        Draws board and everthing on it
        """

        print(str(self.board))
    

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
                self.board.set_item(moved_car.row, moved_car.col - direction + i, None)

            for i in range(moved_car.length):
                self.board.set_item(moved_car.row, moved_car.col + i, moved_car)
                            
        if moved_car.orientation == 'V':
            moved_car.row = moved_car.row + direction

            for i in range(moved_car.length):
                self.board.set_item(moved_car.row - direction + i, moved_car.col, None)

            for i in range(moved_car.length):
                self.board.set_item(moved_car.row + i, moved_car.col, moved_car)

        self.moves.append([car, direction])
        return True


    def build(self, moves):
        for move in moves:
            self.move(move[0], move[1])
        

    def reset(self):
        for move in reversed(self.moves):
            self.move(move[0], -move[1])
        
        self.moves = []


    def previous_move(self):
        if self.moves:
            return self.moves[-1]
        
        return [None, None]


    def is_valid_move(self, car, move):
        """
        Checks for validity of the to be played move
        """

        return move in get_possiblities(car, self.board.get_board())
    

    def get_moves(self):
        """
        Returns list of moves
        """
        return self.moves

    def won(self):
        """
        Returns true when the game is won, if no cars are blocking the exit
        """
        
        car_x = self.cars.get('X')

        # if any spot in the path to the exit is occupied, the game is not won
        if any(get_lane(car_x, self.board.get_board())[car_x.col + car_x.length:]):
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