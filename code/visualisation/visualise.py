from code.classes.game import Game
import copy

import numpy as np
from matplotlib import colors 
import matplotlib.pyplot as plt
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

    plt.figure()

    for move in moves:        
        animation.move(move[0], move[1])

        board = [[colors.to_rgb('k') for i in range(size)] for j in range(size)]

        for car in animation.cars.values():
            for i in range(car.length):
                if car.orientation == 'H':
                    board[car.row][car.col + i] = colors.to_rgb(car.colour)
                if car.orientation == 'V':
                    board[car.row + i][car.col] = colors.to_rgb(car.colour)
            
        plt.imshow(board)
        plt.axis('off')
        
        plt.draw()
        plt.pause(1)
        plt.clf()