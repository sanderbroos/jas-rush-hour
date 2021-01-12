from code.classes.game import Game
# load all utility functions
from code.util import *
from code.algorithms.randomise import * 

if __name__ == "__main__":
    game = Game(6, "data/Rushhour6x6_1.csv")
    game.draw_board()

    # --------------------------- Randomise --------------------------

    best_yet = 9999999
    N = int(input("How many times do you want to run the randomise algorithm?\n"))

    for _ in range(N):
        # create a new game
        game = Game(6, "data/Rushhour6x6_1.csv")
        
        # move cars around randomly until the game is won
        while not game.won():
            car = random_car(game.cars)
            game.move(car.name, random_move(car, game.board))

        # if this solution has the least amount of moves yet, overwrite the output
        if len(game.moves) < best_yet:
            best_yet = len(game.moves)
            game.output()
            game.draw_board()

    game.draw_board()

    # --------------------------- Manual -----------------------------

    # while not game.won():
    #     print('Instructions: Left and down are negative numbers, right and up are positive numbers')
    #     car = input("Please the name of the car that should be moved:\n")
    #     if car == "stop":
    #         break
            
    #     direction = input("Please enter your move from -4 to 4:\n")
    #     game.move(car.upper(), int(direction))
    #     game.draw_board()

    # game.output()


    # --------------------------- test -----------------------------
    
    # print(random_benchmark(100))
