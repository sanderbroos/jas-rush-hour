import copy

class Depth:
     """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, game):
        self.game = copy.deepcopy(game)

        self.states = [copy.deepcopy(self.game)]

        self.best_solution = None
        self.best_value = float('inf')
    
    def get_next_car(self):
        # chose next car
        pass

    def build_children(self, car):
        #  creates all child states and add to a list
        pass

    def check_solution(self):
        # looks for less moves
        pass

    def run(self):
        # runs algorithm untill all possible solutions are fount
        pass    



