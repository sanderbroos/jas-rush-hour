from time import sleep
from sys import stdin

class Manual:
    def __init__(self, game):
        self.game = game


    def run(self):
        print('\nInstructions: Left and down are negative numbers, right and up are positive numbers\nExecute \'python3 main.py < output.csv\' to watch a solution being played (choose the right game first).')
             
        while not self.game.won():
            try:
                self.game.draw_board()
                move = input("Enter the move you want to make in the format \"A,1\": ").split(",") 
                print("", end="\n")
                self.game.move(move[0].upper(), int(move[1]))
                if not stdin.isatty():
                    sleep(1)
            except KeyboardInterrupt as e:
                raise e
            except:
                pass

        self.game.draw_board()
        self.game.output()