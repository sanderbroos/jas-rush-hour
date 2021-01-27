from code.util import get_lane, get_possibilities


def null_heuristic(default=None):
    """
    For comparison - identical to Breadth First Search with Astar.
    """
    return 0


def block_heuristic(game):
    """
    The number of cars blocking the car X.
    """
    car_x = game.cars.get('X')
    lane = get_lane(car_x, game.board.board)[car_x.col + car_x.length:]
    
    return len(lane) - lane.count(None)


def double_block_heuristic(game):
    """
    The number of cars blocking carX + the number of cars
    blocking those cars.
    """
    car_x = game.cars.get('X')
    lane = get_lane(car_x, game.board.board)[car_x.col + car_x.length:]
    blocking_cars = [car for car in lane if car]

    # check if blocking cars are blocked
    blocked_blockingcars = 0
    for car in blocking_cars:
        if not get_possibilities(car, game.board.board):
            blocked_blockingcars +=1
    
    return len(blocking_cars) + blocked_blockingcars


def position_heuristic(current_cars, winning_cars):
    """
    Checks how many current cars are in the same
    position as the cars of the given game.
    """
    value = 0
    for key in current_cars.keys():
        if (current_cars[key].col == winning_cars[key].col and
                current_cars[key].row == winning_cars[key].row):
            value -= 1
                
    return value