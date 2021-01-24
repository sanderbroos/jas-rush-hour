from .randomise import * 
from code.util import clean_moves
from copy import deepcopy


class HillClimber:
    def __init__(self, game):
        self.game = deepcopy(game)
        self.moves = []


    def run(self):
        # initialize any solution
        print("Running Random algorithm 10 times to get a decent \"starting point\" solution...")
        self.moves = Random(self.game, 10).run()

        changes = 1

        # keep repeating until the algorithm doesn't have an effect anymore
        while changes:
            changes = 0
            i = 0
            
            # try to combine any 2 moves, thereby shortening the list of moves by 1
            for move in self.moves:
                j = i + 1

                for next_move in self.moves[j:]:
                    # if two moves involve the same car
                    if self.moves[i][0] == self.moves[j][0]:
                        # try out the new changes on a temporary list
                        new_moves = deepcopy(self.moves)
                        new_moves[i][1] += new_moves.pop(j)[1]

                        self.game.build(new_moves)

                        # see if combining these two moves still makes for a winning solution
                        if self.game.won():
                            # if so, save the changes permanently
                            self.moves = new_moves
                            j -= 1
                            changes += 1
                            print(f"Improving solution... Current # of moves: {len(self.moves):<50}", end='\r')

                        self.game.reset()
                    
                    j += 1

                i += 1

        self.game.build(self.moves)
        self.game.won()

        print(f"Final solution moves length: {len(self.game.get_moves()):<50}")

        self.game.draw_board()
        self.game.output()