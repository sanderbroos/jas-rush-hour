from code.classes.game import Game
from code.algorithms.manual import *
from code.algorithms.depth_first import *
from code.algorithms.breadth_first import *
from code.algorithms.randomise import * 
from code.algorithms.Astar import Astar
from code.algorithms.iterative_deepening import * 
from code.heuristics import *
# load all utility functions
from code.util import *

if __name__ == "__main__":
    game_nr = 0
    while not 1 <= game_nr <= 8:
        game_nr = int(input("Which board do you want to use? (1-8) "))

    games = {1: Game(6, "data/Rushhour6x6_1.csv"),
            2: Game(6, "data/Rushhour6x6_2.csv"),
            3: Game(6, "data/Rushhour6x6_3.csv"),
            4: Game(9, "data/Rushhour9x9_4.csv"),
            5: Game(9, "data/Rushhour9x9_5.csv"),
            6: Game(9, "data/Rushhour9x9_6.csv"),
            7: Game(12, "data/Rushhour12x12_7.csv"),
            8: Game(6, "data/Hardest6x6.csv")}

    game = games[game_nr]
    game.draw_board()

    algorithms = {"M": Manual(game),
                  "R": Random(game),
                  "D": DepthFirst(game),
                  "B": BreadthFirst(game),
                  "I": IterativeDeepening(game),
                  "AS" : Astar(game)}
    
    print("Available algorithms:")
    for key, value in algorithms.items():
        print(f"    {key:>2}: {value.__class__.__name__}")

    algorithm = algorithms[algo_id]
    algorithm.run()
    print()
