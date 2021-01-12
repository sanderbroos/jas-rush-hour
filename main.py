from code.classes.game import Game
# load all utility functions
from code.util import *
from code.algorithms.randomise import * 

if __name__ == "__main__":
    game = Game(6, "data/Rushhour6x6_1.csv")
    print('Instructions: Left and down are negative numbers, right and up are positive numbers')
    game.draw_board()

    while not game.won():
        car = random_car(game.cars)
        move = random_move(car, game.board)
        game.move(car.name, move)
    game.draw_board()




    # while not game.won():
    #     car = input("Please the name of the car that should be moved:\n")
    #     if car == "stop":
    #         break
            
    #     direction = input("Please enter your move from -4 to 4:\n")
    #     game.move(car.upper(), int(direction))
    #     game.draw_board()

    game.output()