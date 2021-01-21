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


if __name__ == "__main__":
    game = Game(6, "data/Rushhour6x6_1.csv")
    board = game.board.board
    cars = game.cars