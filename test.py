from code.classes.game import Game
from code.heuristics import *
from code.algorithms import depth_first as df
from code.algorithms import breadth_first as bf
from code.algorithms.Astar import Astar
# load all utility functions
from code.util import *
from code.algorithms.randomise import * 
import matplotlib.pyplot as plt
import numpy as np
import time
from dataclasses import dataclass, field
import queue
from code.algorithms.modAstar import RanAstar


if __name__ == "__main__":
    game = Game(9, "data/Rushhour9x9_5.csv")
 

    algorithm = RanAstar(game)
    print(len(algorithm.run()))



