from code.algorithms.breadth_first import BreadthFirst
from code.algorithms.randomise import Random, RandomOnce
from copy import deepcopy
from itertools import repeat

class modRandom(Random):

    def run(self, repeats):

        for _ in repeat(None, repeats):

            algorithm = RandomOnce(self.game)
            algorithm.run()
            moves_made = algorithm.game.get_moves()
            self.numb_moves.append(len(moves_made))
        
            if len(moves_made) < self.best_value:
                self.best_moves = moves_made
                self.best_value = len(moves_made)
                algorithm.game.output()

        return self.best_moves


class modBreadthFirst(BreadthFirst):

    def __init__(self, game, end_board):
        super().__init__(game)
        self.end = end_board

    def win(self):
        return str(self.game.board) == self.end

    def run(self):
        """
        Runs the algorithm until all possible states are visited.
        """
        self.enqueue(self.game.get_moves())
        i = 0

        while not self.states.empty():
            self.game.build(self.dequeue())
            i += 1
            print(i)
            
            if self.win():
                return self.game.moves
                
            self.build_children()
            self.game.reset()

        

class RandomBFS():

    def __init__(self, game, repeats, dist):
        self.game = deepcopy(game)
        self.Random = modRandom(game)
        self.BFS = BreadthFirst
        self.random_path = self.get_random_path(repeats)
        self.checkpoints = self.get_checkpoints(dist)
        self.path = []

    def get_random_path(self,repeats):
        random_path = self.Random.run(repeats)
        return random_path
        

    def get_checkpoints(self, dist):
        
        checkpoints = []
        new_game = deepcopy(self.game)
        counter = 0
        end = len(self.random_path)

        if self.random_path:

            for move in self.random_path:
                new_game.move(move[0],move[1])
                counter += 1

                # take board config at intervals and append to list
                if counter % dist == 0 or counter == end:
                    checkpoint = str(new_game.board)
                    checkpoints.append(checkpoint)
        return checkpoints


    def BFS_search(self, game, end_board):
        return modBreadthFirst(game, end_board).run()
    
    def run(self):
        
        for checkpoint in self.checkpoints:
            print(checkpoint)
            # get shortest path between checkpoints
            game = deepcopy(self.game)
            moves = self.BFS_search(game, checkpoint)
            print( moves)
            # upgrade board and path
            for  move in moves:
                self.path.append(move)
                self.game.move(move[0], move[1])

        print(self.path)
        return self.path
