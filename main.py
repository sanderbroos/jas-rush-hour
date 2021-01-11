from code.classes.game import Game
from code.util import get_lane

if __name__ == "__main__":
    game = Game(6, "data/Rushhour6x6_1.csv")
    print('Instructions: Left and down are negative numbers, right and up are positive numbers')
    game.draw_board()
    
    while game.won() is False:
        direction = input("Please enter your move from -4 to 4:\n")
        game.move(int(direction))
        game.draw_board()



