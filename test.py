from code.classes.game import Game
from code.algorithms.modAstar import RanAstar


if __name__ == "__main__":
    game = Game(6, "data/Rushhour6x6_1.csv")
 

    algorithm = RanAstar(game)
    algorithm.run()


