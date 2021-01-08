import csv

from .car import Car


class Board():

    def __init__ (self, size):
        self.size = size
        # load board and everything on it
        
        def load_cars(self, source_file):
            # load dictionary with key name car and value the car 
            # not tested yet!
            cars = {}
            with open(source_file, 'r') as readfile:
                reader = csv.DictReader(readfile)

                for row in reader:
                    if row['car'] == 'X':
                        carX = True
                    else:
                        carX = False
                    cars[row['car']] = Car(row['car'], row['orientation'], row['col'], row['row'], row['length'], carX)

            return cars
            


    def draw_board(self):
        # draw board and everthing on it
        pass
    
    def move(self, direction):
        # move trucks or cars, check is validmove etc the save new place in car class, save moves made for output file
        pass
    
    def won(self):
        # game won, car in space just before gate means game is won
        pass
    
    def is_valid_move(self):
        pass