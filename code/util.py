def get_lane(car, board):
    """
    Gets whole row/col in which the car/truck is located.
    Makes is_valid function easier to read.
    """

    if car.orientation == 'V':
        column = []

        for i in range(0,len(board)):
            column.append(board[i][car.col])

        return column
    
    return board[car.row]


def get_possiblities(car, board):
    """
    gives all possible moves of a car in a given lane
    """

    moves = []
    size = len(board)
    lane = get_lane(car, board)

    if car.orientation == 'H':
        index = car.col
    if car.orientation == 'V':
        index = car.row

    for i in range(1, size - 1):
        if (index + i + car.length <= size and
                lane[index + (i + car.length) - 1] == None):
            moves.append(i)
        else:
            break
    
    for i in range(1, size - 1): 
        if (index - i > -1
                and lane[index - i] == None):
            moves[:0] = [-i]
        else:
            break
        
    return moves

def all_moves(game):
    """ Returns list with all possible moves for all cars 
    like [[car1,move1], [car1,move2], etc]"""
    
    moves = []
    for car in game.cars.keys():
        possibilities = get_possiblities(game.cars.get(car), game.board)

        for move in possibilities:
            moves.append([car, move])

    return moves


def clean_moves(moves):
    i = 0

    while i < len(moves):
        move = moves[i]
        
        # if one car makes two moves directly after each other, combine these moves into 1
        if move[0] == moves[i-1][0]:
            move[1] += moves.pop(i-1)[1]
            i -= 1

        i += 1

    return moves