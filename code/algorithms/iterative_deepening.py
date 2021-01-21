from .depth_first import DepthFirst

class IterativeDeepening:
    def __init__(self, game):
        self.game = game

    def run(self):
        found_solution = False
        depth = 1

        while not found_solution:
            print(f"Maximum depth: {depth}")
            found_solution = DepthFirst(self.game, depth).run()
            depth += 1