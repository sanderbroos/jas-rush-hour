import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def visualise(game, moves):
    """
    Visualise a given rush hour game by animating each move made.
    """
    print("Loading visualisation...\n")
  
    size = game.board.get_size()
    game.reset()
    plt.figure()

    # add three empty moves, so the initial board is shown a little longer
    for move in [["X", 0]] * 3 + moves:
        game.move(move[0], move[1])

        # initialize black background grid of the correct size
        board = [[(0,0,0) for i in range(size)] for j in range(size)]

        # add a rectangle to the plot for each car
        for car in game.cars.values():
            if car.orientation == 'H':
                width = car.length
                height = 1
            elif car.orientation == 'V':
                width = 1
                height = car.length
                
            plt.gca().add_patch(Rectangle(xy=(car.col-0.5, car.row-0.5), 
                                          width=width, 
                                          height=height, 
                                          linewidth=0.3,
                                          edgecolor='k', 
                                          facecolor=car.color))
        
        plt.imshow(board)
        plt.axis('off')
        
        plt.draw()
        plt.pause(0.5)
        plt.clf()