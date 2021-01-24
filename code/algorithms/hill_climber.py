from .randomise import * 
from code.util import clean_moves
from copy import deepcopy


class HillClimber:
    def __init__(self, game):
        self.game = deepcopy(game)
        self.moves = []

    def run(self):
        # initialize any solution
        self.moves = Random(self.game).run()
        print()

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
                        new_moves = deepcopy(self.moves)
                        new_moves[i][1] += new_moves.pop(j)[1]

                        self.game.build(new_moves)

                        # see if combining these two moves still makes for a winning solution
                        if self.game.won():
                            print(f"Solution length: {len(self.moves)}        ", end='\r')
                            self.moves = deepcopy(new_moves)
                            j -= 1
                            changes += 1

                        self.game.reset()
                    
                    j += 1

                i += 1
        
        self.moves = clean_moves(self.moves)
        self.game.build(self.moves)

        print(f"Final solution moves length: {len(self.game.get_moves())}        ")

        self.game.draw_board()
        self.game.output()