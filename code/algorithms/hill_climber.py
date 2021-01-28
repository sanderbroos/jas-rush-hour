from .randomise import Random
from copy import deepcopy


class HillClimber:
    """
    A Hill Climber algorithm that uses a randomly generated solution
    and iteratively tries to combine moves together for improvement.
    """
    def __init__(self, game):
        self.game = deepcopy(game)
        self.moves = []


    def try_combining(self, i, j, flipped):
        """
        Tries to combine the cars from self.moves at index i and j. If
        it's successful and doesn't change the outcome of the game, return True.
        """
        # if two different moves involve the same car
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
                return True

        return False


    def combine_moves(self, flipped):
        """
        Tries to combine any two moves in self.moves.
        """
        changes = 0
        length = len(self.moves)
        i = 0
        
        # can't use for-loop, since it's deleting elements from the list
        while i < length:
            j = i + 1

            while j < length:
                # try to combine car i and car j
                if self.try_combining(i, j, flipped=flipped):
                    if flipped:
                        i -= 1

                    j -= 1
                    length -= 1
                    changes += 1

                    print("Improving solution... Current:",
                          f"{len(self.moves)} {'moves':<50}", end='\r')
                    
                self.game.reset()
                j += 1

            i += 1
        
        return changes


    def remove_redundant_moves(self):
        """
        For every move, check if it has an effect on the game.
        If not, remove it.
        """
        i = 0
        changes = 0
        length = len(self.moves)

        # can't use for-loop, since it's deleting elements from the list
        while i < length:
            move = self.moves[i]

            # remove this item from the list
            self.moves.pop(i)

            # execute the new list of moves
            self.game.build(self.moves)

            # see if this still makes for a winning solution
            if self.game.won():
                changes += 1
                i -= 1
                length -= 1

                print("Improving solution... Current:",
                       f"{len(self.moves)} {'moves':<50}", end='\r')
            else:
                # otherwise, add the move back
                self.moves.insert(i, move)

            self.game.reset()
            i += 1

        return changes


    def run(self):
        """
        Runs the algorithm by shortening a random solution.
        """
        # initialize any solution
        print("Running Random algorithm multiple times to get a decent",
              "\"starting point\" solution...")
        self.moves = Random(self.game, repeats=200, fastest=True).run()

        # keep trying to shorten the list until the algorithm has no effect anymore
        changes = 1
        while changes > 0:
            changes = 0

            # shorten the moves in three different ways
            changes += self.remove_redundant_moves()
            changes += self.combine_moves(flipped=False)
            changes += self.combine_moves(flipped=True)

        # execute the moves and perform the final move to the exit
        self.game.build(self.moves)
        self.game.won()

        print(f"Final solution: {len(self.game.get_moves())} {'moves':<50}")

        self.game.draw_board()

        return self.game.get_moves()