from .randomise import Random 
from copy import deepcopy


class HillClimber:
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


    def hill_climb_once(self, flipped):
        """
        Goes through the list of moves once.
        Tries to combine any two moves.
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
                            f"{len(self.moves)} {'moves':<50}", sep='', end='\r')
                    
                self.game.reset()
                j += 1

            i += 1
        
        return changes


    def hill_climb(self, flipped=False):
        """
        Keeps going through the entire list until the algorithm has no effect.
        """
        while self.hill_climb_once(flipped=flipped):
            pass


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
        print("Running Random algorithm multiple times to get a decent ",
                "\"starting point\" solution...", sep="")
        self.moves = Random(self.game, repeats=200, fastest=True).run()

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