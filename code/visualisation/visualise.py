import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def visualise(game, moves):
    """
    Visualise a rush hour game by animating each move made
    """
    print("Loading visualisation...\n")
  
    size = game.board.size
    game.reset()

    plt.figure()

    for move in [["A", 0], ["A", 0]] + moves:        
        game.move(move[0], move[1])

        board = [[(0,0,0) for i in range(size)] for j in range(size)]

        for car in game.cars.values():
            if car.orientation == 'H':
                plt.gca().add_patch(Rectangle((car.col-0.5, car.row-0.5),car.length,1,linewidth=0.3,edgecolor='k',facecolor=car.colour))
            elif car.orientation == 'V':
                plt.gca().add_patch(Rectangle((car.col-0.5, car.row-0.5),1,car.length,linewidth=0.3,edgecolor='k',facecolor=car.colour))
        
        plt.imshow(board)
        plt.axis('off')
        
        plt.draw()
        plt.pause(0.5)
        plt.clf()