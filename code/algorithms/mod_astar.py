from code.algorithms.randomise import Random
from code.algorithms.a_star import Astar
from code.heuristics import position_heuristic
from copy import deepcopy


class ModAstar(Astar):
    """
    Modified Astar algortihm using the winning cars position heuristic.
    """
    def __init__(self, game, cars, str_board):
        super().__init__(game)
        self.end_cars = cars
        self.end_board = str_board


    def set_priority(self):
        """	
        Calculate the heuristic by checking how many current cars are in	
        the same position as the cars of the given game.	
        """
        return position_heuristic(self.game.cars, self.end_cars)


    def win(self):
        """
        The algorithm stops when the given board is reached.
        """
        return str(self.game.board) == self.end_board


class RanAstar():
    """
    An algorithm that uses a randomly generated solution, sets checkpoints
    and finds the shortest paths between those checkpoints using the
    ModAstar algorithm.
    """
    def __init__(self, game):
        self.game = deepcopy(game)
        self.path = []
        self.checkpoints = []


    def get_checkpoints(self, dist):
        """
        Sets checkpoints with a fixed distance on a path.
        """
        new_game = deepcopy(self.game)
        counter = 0
        end = len(self.path)

        for move in self.path:
            new_game.move(move[0], move[1])
            counter += 1

            if counter % dist == 0 or counter == end:
                self.checkpoints.append([str(new_game.board), new_game.cars])

            
    def run(self):
        """
        Runs the RanAstar algorithm.
        """
        # initialize any solution
        print("Running Random algorithm multiple times to get a decent",
              "\"starting point\" solution...")
        self.path = Random(self.game, repeats=200, fastest=True).run()
        self.get_checkpoints(dist=6)
        self.path = []

        # search for shortest path between checkpoints
        for checkpoint in self.checkpoints:
            game = deepcopy(self.game)
            moves = ModAstar(game, checkpoint[1], checkpoint[0]).run()

            # update game
            self.game.build(moves)
            self.path += moves

            # see the number of moves needed per checkpoint
            self.game.moves = []
        
        print(f"Final solution: {len(self.path)}")
        return self.path