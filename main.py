from code.classes.game import Game
from code.algorithms import depth_first as df
from code.algorithms import breadth_first as bf
# load all utility functions
from code.util import *
from code.algorithms.randomise import * 
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    game = Game(6, "data/Rushhour6x6_1.csv")
    game.draw_board()

    # --------------------------- Randomise --------------------------

    # best_yet = 9999999
    # N = int(input("How many times do you want to run the randomise algorithm?\n"))

    # for _ in range(N):
    #     # create a new game
    #     game = Game(6, "data/Rushhour6x6_1.csv")
        
    #     # move cars around randomly until the game is won
    #     while not game.won():
    #         car = random_car(game.cars)
    #         game.move(car.name, random_move(car, game.board))

    #     # if this solution has the least amount of moves yet, overwrite the output
    #     if len(game.get_moves()) < best_yet:
    #         best_yet = len(game.get_moves())
    #         game.output()
    #         game.draw_board()

    # game.draw_board()

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
    
    # bench = Benchmark_random(game,100)
    # print(bench[0])
    
    # --------------------------- Depth first ----------------------

    depth_first = df.DepthFirst(game)
    depth_first.run()
    
    # --------------------------- Breadth first ----------------------

    # breadth_first = bf.BreadthFirst(game)
    # breadth_first.run()