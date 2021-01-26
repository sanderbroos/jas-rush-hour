from .randomise import Random 
from copy import deepcopy


class HillClimber:
    def __init__(self, game):
        self.game = deepcopy(game)
        self.moves = []


    def hill_climb(self, flipped = False):
        """
        Try to combine any 2 moves, which shortens the list of moves by 1.
        """
        changes = 1

        # keep repeating until the algorithm doesn't have an effect anymore
        while changes:
            changes = 0
            length = len(self.moves)
            i = 0
            
            # can't use for-loop, since it's deleting elements from the list
            while i < length:
                j = i + 1

                while j < length:
                    # if two moves involve the same car
                    if i != j and self.moves[i][0] == self.moves[j][0]:
                        # try out the new changes on a temporary list
                        new_moves = deepcopy(self.moves)

                        # combine move i and j into either j's index or i's index 
                        if flipped:
                            new_moves[j][1] += new_moves.pop(i)[1]
                        else:
                            new_moves[i][1] += new_moves.pop(j)[1]

                        # execute the new list of moves
                        self.game.build(new_moves)

                        # see if this still makes for a winning solution
                        if self.game.won():
                            # if so, save the changes permanently
                            self.moves = new_moves
                            
                            if flipped:
                                i -= 1

                            j -= 1
                            length -= 1
                            changes += 1

                            print(f"Improving solution... Current: {len(self.moves)} {'moves':<50}", end='\r')
                        
                        self.game.reset()
                    
                    j += 1

                i += 1


    def remove_redundant_moves(self):
        """
        For every move, check if it has an effect on the game.
        If not, remove it.
        """
        i = 0
        length = len(self.moves)

        # can't use for-loop, since it's deleting elements from the list
        while i < length:
            # try out the new changes on a temporary list
            new_moves = deepcopy(self.moves)

            # remove this item from the list
            new_moves.pop(i)

            # execute the new list of moves
            self.game.build(new_moves)

            # see if this still makes for a winning solution
            if self.game.won():
                # if so, save the changes permanently
                self.moves = new_moves
                i -= 1
                length -= 1

            self.game.reset()
            i += 1


    def run(self):
        """
        Runs the algorithm by shortening a random solution.
        """
        # initialize any solution
        print("Running Random algorithm multiple times to get a decent \"starting point\" solution...")
        self.moves = Random(self.game, 200, fastest=True).run()

        # shorten the moves in three different ways
        self.hill_climb(flipped=False)
        self.hill_climb(flipped=True)
        self.remove_redundant_moves()

        # execute the moves and perform the final move to the exit
        self.game.build(self.moves)
        self.game.won()

        print(f"Final solution: {len(self.game.get_moves())} {'moves':<50}")

        self.game.draw_board()

        return self.game.get_moves()