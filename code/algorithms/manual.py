class Manual:
    """
    Lets the user play the game by entering moves.
    """
    def __init__(self, game):
        self.game = game


    def run(self):
        """
        Lets the user enter moves until they have solved the game.
        """
        print("Instructions: Left and up are negative numbers,",
              "right and down are positive numbers\nExecute",
              "\'python3 main.py < docs/output.csv\' to watch a solution",
              "being played (choose the right game first in the code).")
             
        while not self.game.won():
            move = input("Enter the move you want to make in the format \"A,1\": ").split(",") 
            
            if not self.game.move(move[0].upper(), move[1]):
                print("\nOMG.. Enter a valid move, please.")
            else:
                self.game.draw_board()
    
        return self.game.get_moves()