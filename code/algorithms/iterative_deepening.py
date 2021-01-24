from .depth_first import DepthFirst

class IterativeDeepening:
    def __init__(self, game):
        self.game = game


    def run(self):
        depth = 1
        solution = None

        while not solution:
            solution = DepthFirst(self.game, depth).run()
            print(f"\nMaximum depth: {depth}")
            depth += 1

        return solution