import numpy as np
from matplotlib import colors 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def visualise(game):
    """
    Visualise a rush hour game
    """
    print("Loading visualisation...\n")
    # I can sort the moves or loop like draw board
    # Do i want data to be a list?
    # how do i want to identify the cars in the list? how do i give the cars a colour
    # get loop from the old draw_board in game
    # Probleem nu is dat alleen een board gegeven niet alle zetten van een game
    # is het mogelijk om een grid te hebben zonder lijnen door auto’s heen.
    
    # loopen over lijst moves van output of game.moves. Elke iteratie van loop visualisatie plotten met toegepaste move, 
    # deze plots achter elkaar zetten in een gifje om verloop van spel te kunnen laten zien.
    # nadelen: plot weergave gaat sws trippen en veel 'dubbel code om move te kunnen toepassen'
    
    # create get size in boaard and try to remove hardcoded size? wont work cause need size to render board?
    
    size = game.board.size
    # data needs to be an 2D array of floats which represent colours, how do i turn a car name to a colour?

    # board = [[colors.to_rgb('k') for i in range(size)] for j in range(size)]

    # for car in game.cars.values():
    #     for i in range(car.length):
    #         if car.orientation == 'H':
    #             board[car.row][car.col + i] = colors.to_rgb(car.name)
    #         if car.orientation == 'V':
    #             board[car.row + i][car.col] = colors.to_rgb(car.name)
    # print(board)
        # create new list in list here
        

    # chose colours for the cars
    #my_cmap = ListedColormap(['r', 'g', 'b'])

    #my_cmap.set_bad(color='k', alpha=0)

    # test imshow
    np.random.seed(19680801)
    X = 10*np.random.rand(size, size)
    print(X)
    fig, ax = plt.subplots(tight_layout=True)
    ax.imshow(X)
    numrows, numcols = X.shape

    #ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, size, 0, size], zorder=0)

    ax.axis('off')
    
    plt.show()