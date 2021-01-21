from code.util import *


def null_heuristic(game):
    return 0

def block_heuristic(game):
    """
    The number of cars blocking the carX
    """

    car_x = game.cars.get('X')
    lane = get_lane(car_x, game.board.board)[car_x.col + car_x.length:]
    
    return len(lane) - lane.count(None)


def double_block_heuristic(game):
    """
    The number of cars blocking carX + the number of cars
    blocking the previous mentioned cars
    """

    car_x = game.cars.get('X')
    lane = get_lane(car_x, game.board.board)[car_x.col + car_x.length:]
    blocking_cars = [car for car in lane if car]

    # check if blocking cars are blocked
    blocked_blockingcars = 0
    for car in blocking_cars:
        if not get_possiblities(car,game.board.board):
            blocked_blockingcars +=1
    
    return len(blocking_cars) + blocked_blockingcars

