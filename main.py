from code.classes.game import Game
<<<<<<< HEAD
from code.util import get_lane, get_possiblities
=======
from code.util import *
>>>>>>> 13a23e2c0cbc7c96c933fa1967b3410deb5d2244

if __name__ == "__main__":
    game = Game(6, "data/Rushhour6x6_1.csv")
    print('Instructions: Left and down are negative numbers, right and up are positive numbers')
    game.draw_board()
<<<<<<< HEAD
=======
    
    while not game.won():
        car = input("Please the name of the car that should be moved:\n")
        direction = input("Please enter your move from -4 to 4:\n")
        game.move(car.upper(), int(direction))
        game.draw_board()



>>>>>>> 13a23e2c0cbc7c96c933fa1967b3410deb5d2244
