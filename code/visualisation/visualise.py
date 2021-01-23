import numpy as np
from matplotlib import colors 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def visualise(game):
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
    board = [[colors.to_rgb('k') for i in range(size)] for j in range(size)]

    for car in game.cars.values():
        for i in range(car.length):
            if car.orientation == 'H':
                board[car.row][car.col + i] = colors.to_rgb(car.colour)
            if car.orientation == 'V':
                board[car.row + i][car.col] = colors.to_rgb(car.colour)
        
    fig, ax = plt.subplots(tight_layout=True)
    ax.imshow(board)
    ax.axis('off')
    plt.show()