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
    Visualise a rush hour game
    """
    print("Loading visualisation...\n")
    # Probleem nu is dat alleen een board gegeven niet alle zetten van een game
    # is het mogelijk om een grid te hebben zonder lijnen door auto’s heen.
    
    # loopen over lijst moves van output of game.moves. Elke iteratie van loop visualisatie plotten met toegepaste move, 
    # deze plots achter elkaar zetten in een gifje om verloop van spel te kunnen laten zien.
    # nadelen: plot weergave gaat sws trippen als er veel moves zijn en veel 'dubbel code om move te kunnen toepassen'
    
    # create get size in boaard and try to remove hardcoded size? wont work cause need size to render board?
    size = game.board.size
    # lijst moves is leeg, gebruik output file
    # print(game.get_moves())
    
    animation = copy.deepcopy(game)
    animation.reset()

    # fig,ax = plt.subplots(1)
    plt.figure()

    for move in [["A", 0], ["A", 0]] + moves:        
        animation.move(move[0], move[1])

        board = [[colors.to_rgb('k') for i in range(size)] for j in range(size)]

        for car in animation.cars.values():
            if car.orientation == 'H':
                plt.gca().add_patch(Rectangle((car.col-0.5, car.row-0.5),car.length,1,linewidth=0.3,edgecolor='k',facecolor=car.colour))
            if car.orientation == 'V':
                plt.gca().add_patch(Rectangle((car.col-0.5, car.row-0.5),1,car.length,linewidth=0.3,edgecolor='k',facecolor=car.colour))
        
        
        plt.imshow(board)
        plt.axis('off')
        
        plt.draw()
        plt.pause(0.5)
        plt.clf()