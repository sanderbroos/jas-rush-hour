from .depth_first import DepthFirst


class IterativeDeepening:
    """
    Algorithm that repeats Depth First Search with increasing depths until 
    a solution is found.
    """
    def __init__(self, game):
        self.game = game


    def run(self):
        """
        Runs the algorithm until a solution is found.
        """
        depth = 1
        solution = None

        # run depth first search with increasing depth until a solution is found
        while not solution:
            solution = DepthFirst(self.game, depth).run()
            print(f"\nMaximum depth: {depth}")
            depth += 1

        return solution