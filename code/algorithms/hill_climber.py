from .randomise import Random 
from copy import deepcopy


class HillClimber:
    def __init__(self, game):
        self.game = deepcopy(game)
        self.moves = []


    def hill_climb(self, reverse = False):
        changes = 1

        # keep repeating until the algorithm doesn't have an effect anymore
        while changes:
            changes = 0
            i = 0

            length = len(self.moves)
            
            # try to combine any 2 moves, thereby shortening the list of moves by 1
            while i < length:
                j = i + 1

                while j < length:
                    # if two moves involve the same car
                    if self.moves[i][0] == self.moves[j][0]:
                        # try out the new changes on a temporary list
                        new_moves = deepcopy(self.moves)

                        if reverse:
                            new_moves[j][1] += new_moves.pop(i)[1]
                        else:
                            new_moves[i][1] += new_moves.pop(j)[1]

                        self.game.build(new_moves)

                        # see if combining these two moves still makes for a winning solution
                        if self.game.won():
                            # if so, save the changes permanently
                            self.moves = new_moves
                            
                            if reverse:
                                i -= 1

                            j -= 1
                            length -= 1
                            changes += 1

                            print(f"Improving solution... Current: {len(self.moves)} {'moves':<50}", end='\r')
                        
                        self.game.reset()
                    
                    j += 1

                i += 1


    def remove_redundant_moves(self):
        i = 0
        length = len(self.moves)

        while i < length:
            new_moves = deepcopy(self.moves)
            new_moves.pop(i)

            self.game.build(new_moves)

            if self.game.won():
                self.moves = new_moves
                i -= 1
                length -= 1

            self.game.reset()
            i += 1


    def run(self):
        # initialize any solution
        print("Running Random algorithm multiple times to get a decent \"starting point\" solution...")
        self.moves = Random(self.game, 200, fastest=True).run()

        self.hill_climb()
        self.hill_climb(reverse = True)
        self.remove_redundant_moves()

        self.game.build(self.moves)
        self.game.won()

        print(f"Final solution: {len(self.game.get_moves())} {'moves':<50}")

        self.game.draw_board()

        return self.game.get_moves()