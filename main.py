from code.classes.game import Game
from code.algorithms.manual import *
from code.algorithms.depth_first import *
from code.algorithms.breadth_first import *
from code.algorithms.randomise import * 
from code.algorithms.Astar import Astar
from code.algorithms.iterative_deepening import * 
from code.heuristics import *
from code.visualisation import visualise as vis
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
    # draw board zie je momenteel erg slecht
    game.draw_board()

    algorithms = {"M": Manual(game),
                  "R": Random(game),
                  "D": DepthFirst(game),
                  "B": BreadthFirst(game),
                  "I": IterativeDeepening(game),
                  "S": Astar(game)}

    print("Available algorithms:")
    for key, value in algorithms.items():
        print(f"    {key:>2}: {value.__class__.__name__}")

    algo_id = "None"
    while algo_id not in algorithms:
        algo_id = input("Which algorithm do you want to use? ").upper()
    print()

    if algo_id == "S":
        heuristics = { "NULL" : "No heuristic (BreathFirst)",
                        "BL" : "Blocking cars",
                        "2BL" : "Double blocking cars"}

        print("Available heuristics:")
        for key, value in heuristics.items():
            print(f"    {key:>2}: {value}")
        
        heuristic = "None"
        while heuristic not in heuristics:
            heuristic = input(f"Which heuristic do you want to use? Possiblities are: {', '.join(heuristics)}. ").upper()

        Astar(game, heuristic).run()

    else:
        algorithm = algorithms[algo_id]
        algorithm.run()
    print()

    # --------------------------- Visualisation --------------------------------
    # vis.visualise(game)
