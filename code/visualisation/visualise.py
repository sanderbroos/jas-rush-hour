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

    # Add two empty moves, so the initial board is shown a little longer
    for move in [["X", 0], ["X", 0]] + moves:
        game.move(move[0], move[1])

        # initialize black background grid of the correct size
        board = [[(0,0,0) for i in range(size)] for j in range(size)]

        # add a rectangle to the plot for each car
        for car in game.cars.values():
            if car.orientation == 'H':
                plt.gca().add_patch(Rectangle((car.col-0.5, car.row-0.5),car.length,1,linewidth=0.3,edgecolor='k',facecolor=car.color))
            elif car.orientation == 'V':
                plt.gca().add_patch(Rectangle((car.col-0.5, car.row-0.5),1,car.length,linewidth=0.3,edgecolor='k',facecolor=car.color))
        
        plt.imshow(board)
        plt.axis('off')
        
        plt.draw()
        plt.pause(0.5)
        plt.clf()