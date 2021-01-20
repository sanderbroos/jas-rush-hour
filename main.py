from code.classes.game import Game
from code.heuristics import *
from code.algorithms import depth_first as df
from code.algorithms import breadth_first as bf
# load all utility functions
from code.util import *
from code.algorithms.randomise import * 
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    game_nr = 0
    while not 1 <= game_nr <= 7:
        try:
            game_nr = int(input("Which board do you want to use? (1-7)\n"))
        except:
            pass

    game = {1: Game(6, "data/Rushhour6x6_1.csv"),
            2: Game(6, "data/Rushhour6x6_2.csv"),
            3: Game(6, "data/Rushhour6x6_3.csv"),
            4: Game(9, "data/Rushhour9x9_4.csv"),
            5: Game(9, "data/Rushhour9x9_5.csv"),
            6: Game(9, "data/Rushhour9x9_6.csv"),
            7: Game(12, "data/Rushhour12x12_7.csv")}[game_nr]
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

    # --------------------------- Randomise -----------------------------
    # N is amount of iterations to run randomise algorithm
    # N = 100
    # randomiser = RandomAlgorithm(game)
    # bench = randomiser.Benchmark_random(game, N)
    # print(bench[0])
    
    # --------------------------- Depth first ----------------------

    #depth_first = df.DepthFirst(game)
    #depth_first.run()
    
    # --------------------------- Breadth first ----------------------

    breadth_first = bf.BreadthFirst(game)
    breadth_first.run()


    # print(double_block_heuristic(game))
