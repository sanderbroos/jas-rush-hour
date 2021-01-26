import copy

import numpy as np

import matplotlib
#matplotlib.use('agg')  

from matplotlib import colors 
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import ListedColormap

def visualise(game, moves):
    """
    Visualise a rush hour game by animating each move made
    """
    print("Loading visualisation...\n")
  
    size = game.board.size
    animation = copy.deepcopy(game)
    animation.reset()

    plt.figure()

    # add two empty moves, so the initial board is shown a little longer
    for move in [["X", 0], ["X", 0]] + moves:
        game.move(move[0], move[1])

        board = [[colors.to_rgb('k') for i in range(size)] for j in range(size)]

        for car in animation.cars.values():
            if car.orientation == 'H':
                plt.gca().add_patch(Rectangle((car.col-0.5, car.row-0.5),
                                                car.length, 1, linewidth=0.3, 
                                                edgecolor='k', facecolor=car.colour))
            if car.orientation == 'V':
                plt.gca().add_patch(Rectangle((car.col-0.5, car.row-0.5), 1, 
                                                car.length,linewidth=0.3,
                                                edgecolor='k', facecolor=car.colour))
             
        plt.imshow(board)
        plt.axis('off')
        
        plt.draw()
        plt.pause(0.5)
        plt.clf()