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
