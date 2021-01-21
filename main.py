from code.classes.game import Game
from code.algorithms.manual import *
from code.algorithms.depth_first import *
from code.algorithms.breadth_first import *
from code.algorithms.randomise import * 
from code.heuristics import *
# load all utility functions
from code.util import *

if __name__ == "__main__":
    game_nr = 0
    while not 1 <= game_nr <= 7:
        game_nr = int(input("Which board do you want to use? (1-7) "))

    game = {1: Game(6, "data/Rushhour6x6_1.csv"),
            2: Game(6, "data/Rushhour6x6_2.csv"),
            3: Game(6, "data/Rushhour6x6_3.csv"),
            4: Game(9, "data/Rushhour9x9_4.csv"),
            5: Game(9, "data/Rushhour9x9_5.csv"),
            6: Game(9, "data/Rushhour9x9_6.csv"),
            7: Game(12, "data/Rushhour12x12_7.csv")}[game_nr]

    algorithms = {"M": Manual(game),
                  "R": Random(game),
                  "BR": BenchmarkRandom(game),
                  "DF": DepthFirst(game),
                  "BF": BreadthFirst(game)}
                  
    print("Available algorithms:")
    for key, value in algorithms.items():
        print(f"    {key}: {value.__class__.__name__}")

    algorithm = "None"
    while algorithm not in algorithms:
        algorithm = input("Which algorithm do you want to use? ").upper()

    algorithms[algorithm].run()