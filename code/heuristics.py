from code.util import *

def block_heuristic(game):
    """
    The number of cars blocking the carX
    """

    car_x = game.cars.get('X')
    lane = get_lane(car_x, game.board.board)[car_x.col + car_x.length:]
    
    return len(lane) - lane.count(None)