def get_lane(car, board):
    """
    Gets whole row/col in which the car/truck is located.
    Makes is_valid function easier to read.
    """
    
    row = car.row
    col = car.col
    array = []

    if car.orientation == 'V':
        for i in range(0,len(board)):
            array.append(board[i][col])
        return array
    
    return board[row]


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
                lane[index + (i + car.length) - 1] is None):
            moves.append(i)
        else:
            break
    
    for i in range(1, size - 1): 
        if (index - i > -1
                and lane[index - i] is None):
            moves[:0] = [-i]
        else:
            break
        
    return moves
