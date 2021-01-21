from code.classes.game import Game
from code.algorithms.manual import *
from code.algorithms.depth_first import *
from code.algorithms.breadth_first import *
from code.algorithms.randomise import * 
from code.heuristics import *
# load all utility functions
from code.util import *

if __name__ == "__main__":
    # set both to 0 to let the user choose
    game_nr = 0
    algo_id = 0

    games = {1: Game(6, "data/Rushhour6x6_1.csv"),
             2: Game(6, "data/Rushhour6x6_2.csv"),
             3: Game(6, "data/Rushhour6x6_3.csv"),
             4: Game(9, "data/Rushhour9x9_4.csv"),
             5: Game(9, "data/Rushhour9x9_5.csv"),
             6: Game(9, "data/Rushhour9x9_6.csv"),
             7: Game(12, "data/Rushhour12x12_7.csv"),
             8: Game(6, "data/Hardest6x6.csv")}

    while game_nr not in games:
        game_nr = int(input("Which board do you want to use? (1-8) "))

    game = games[game_nr]

    algorithms = {"M": Manual(game),
                  "R": Random(game),
                  "BR": BenchmarkRandom(game),
                  "DF": DepthFirst(game),
                  "BF": BreadthFirst(game)}
                  
    print("\nAvailable algorithms:")
    for key, value in algorithms.items():
        print(f"    {key:>2}: {value.__class__.__name__}")
    
    while algo_id not in algorithms:
        algo_id = input("Which algorithm do you want to use? ").upper()
    print()

    algorithm = algorithms[algo_id]
    algorithm.run()