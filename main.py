from code.classes.game import Game
from code.algorithms.manual import Manual
from code.algorithms.depth_first import DepthFirst
from code.algorithms.breadth_first import BreadthFirst
from code.algorithms.randomise import Random
from code.algorithms.Astar import Astar
from code.algorithms.iterative_deepening import IterativeDeepening
from code.algorithms.hill_climber import HillClimber
from code.visualisation.visualise import visualise
from code.util import output

from time import time

if __name__ == "__main__":
    # set both to None to let the user choose - can also be filled in here to skip input
    board = None
    algo_id = None
    heuristic = None

    # the boards that can be chosen with a Game object initialized for that board
    games = {'1': Game(size=6,  source_file="data/Rushhour6x6_1.csv"),
             '2': Game(size=6,  source_file="data/Rushhour6x6_2.csv"),
             '3': Game(size=6,  source_file="data/Rushhour6x6_3.csv"),
             '4': Game(size=9,  source_file="data/Rushhour9x9_4.csv"),
             '5': Game(size=9,  source_file="data/Rushhour9x9_5.csv"),
             '6': Game(size=9,  source_file="data/Rushhour9x9_6.csv"),
             '7': Game(size=12, source_file="data/Rushhour12x12_7.csv"),
             '8': Game(size=6,  source_file="data/Hardest6x6.csv")}

    while board not in games:
        board = input("Which board do you want to use? (1-8) ")

    game = games[board]
    game.draw_board()

    # initialize all the algorithms that can be chosen
    algorithms = {'M': Manual(game),
                  'R': Random(game),
                  'B': BreadthFirst(game),
                  'D': DepthFirst(game),
                  'I': IterativeDeepening(game),
                  'H': HillClimber(game),
                  'A': Astar(game)}

    # show which letter to type for each available algorithm
    print("\nAvailable algorithms:")
    for key, value in algorithms.items():
        print(f"    {key:>2}: {value.__class__.__name__}")

    while algo_id not in algorithms:
        algo_id = input("Which algorithm do you want to use? ").upper()

    algorithm = algorithms[algo_id]
    # show a bold header that shows which algorithm was chosen
    print(f"\n\u001b[1m {algorithm.__class__.__name__} \u001b[0m\n")
    
    heuristics = {'NULL': "No heuristic (BreathFirst)",
                  'BL' : "Blocking car",
                  '2BL' : "Double blocking cars",}

    # only Astar uses heuristics
    if algorithm.__class__.__name__ == 'Astar':
        print("Available heuristics:")
        for key, value in heuristics.items():
            print(f"    {key:>2}: {value}")

        while heuristic not in heuristics:
            heuristic = input("Which heuristic do you want to use? ").upper()
        
        algorithm.__init__(game, heuristic)

        # show a bold header that shows which algorithm was chosen
        print(f"\n\u001b[1m {heuristics[heuristic]} \u001b[0m\n")

    # record how long it took for the algorithm to finish
    start = time()
    solution = algorithm.run()
    print(f"\nTotal time: {time() - start:.1f} s")

    # if there is a solution, write it to output.csv and animate it
    if solution:
        output(solution)

        if input("\nDo you want to see an animation of the solution? y/n ") == "y":
            visualise(game, solution)