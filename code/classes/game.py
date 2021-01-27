import csv
from .board import Board
from .car import Car
from code.util import clean_moves, get_lane, get_possiblities, direction_to_int


class Game:
    """
    Class which facilitates the playability of the game.
    """
    def __init__ (self, size, source_file):
        self.cars = self.load_cars(source_file)
        self.board = Board(size, self.cars)
        self.moves = []


    def load_cars(self, source_file):
        """
        Returns dictionary with the names of the cars as key and the Car object as value.
        """
        cars = {}
        with open(source_file, 'r') as readfile:
            reader = csv.DictReader(readfile)

            for row in reader:
                cars[row['car']] = Car(row['car'], row['orientation'], int(row['col']) - 1, int(row['row']) - 1, int(row['length']))

        return cars


    def draw_board(self):
        """
        Prints a string representation of the board.
        """
        print(f"\n{str(self.board)}")
    

    def move(self, car, direction):
        """
        If the move is vaild, moves the car and saves the move
        """
        moved_car = self.cars.get(car)
        direction = direction_to_int(direction)

        if not (moved_car and direction and self.is_valid_move(moved_car, direction)):
            return False

        # first remove the car from the board, then re-add it in its new position
        if moved_car.orientation == 'H':
            for i in range(moved_car.length):
                self.board.set_item(moved_car.row, moved_car.col + i, None)
            
            moved_car.col = moved_car.col + direction 

            for i in range(moved_car.length):
                self.board.set_item(moved_car.row, moved_car.col + i, moved_car)
        elif moved_car.orientation == 'V':
            for i in range(moved_car.length):
                self.board.set_item(moved_car.row + i, moved_car.col, None)

            moved_car.row = moved_car.row + direction

            for i in range(moved_car.length):
                self.board.set_item(moved_car.row + i, moved_car.col, moved_car)

        # move is successful, so add it to the list
        self.moves.append([car, direction])

        return True


    def build(self, moves):
        """
        Gets a list of moves as input and executes them all in quick succession.
        """
        for move in moves:
            self.move(move[0], move[1])
        

    def reset(self):
        """
        Resets the board to its initial state by undoing all the moves.
        """
        for move in reversed(self.moves):
            self.move(move[0], -move[1])
        
        self.moves = []


    def is_valid_move(self, car, move):
        """
        Checks for validity of a given move on a given car.
        """
        return move in get_possiblities(car, self.board.get_board())
    

    def get_moves(self):
        """
        Returns the list of moves.
        """
        return self.moves


    def won(self):
        """
        Returns true when the game is won, if no cars are blocking the exit
        """
        car_x = self.cars.get('X')

        # if any spot in the path forward to the exit is occupied, the game is not won
        if any(get_lane(car_x, self.board.get_board())[car_x.col + car_x.length:]):
            return False

        # otherwise the path is free, so move the car to the exit
        self.move(car_x.name, self.board.get_size() - car_x.col - car_x.length)
        self.moves = clean_moves(self.moves)

        return True