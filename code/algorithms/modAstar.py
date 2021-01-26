from code.algorithms.randomise import Random
from code.algorithms.hill_climber import HillClimber
from code.algorithms.Astar import Astar
from code.heuristics import position_heuristic
from copy import deepcopy



class modAstar(Astar):
    
    def __init__(self, game, cars, str_board):
        super().__init__(game)
        self.end_cars = cars
        self.end_board = str_board

    def set_priority(self,game):
        return position_heuristic(game.cars, self.end_cars)

    # def set_priority(self,game):
    #     return 0
    
    def win(self):
        current_board = str(self.game.board)
        return current_board == self.end_board
    

class RanAstar():

    def __init__(self, game):
        self.game = deepcopy(game)
        self.path = []
        self.checkpoints = []


    def get_checkpoints(self, dist):
        
        new_game = deepcopy(self.game)
        counter = 0
        end = len(self.path)

        if self.path:
            for move in self.path:
                new_game.move(move[0],move[1])
                counter += 1

                if counter % dist == 0 or counter == end:
                    self.checkpoints.append([str(new_game.board), new_game.cars])

            
    def run(self):
        # initialize any solution
        #self.path = HillClimber(self.game).run()
        self.path = Random(self.game,5).run()
        self.get_checkpoints(6)
        self.path = []

        for checkpoint in self.checkpoints:
            game = deepcopy(self.game)
            moves = modAstar(game, checkpoint[1], checkpoint[0]).run()
 
            for move in moves:
                self.game.move(move[0], move[1])
                self.path.append(move)
            self.game.moves = []
        
        return self.path
