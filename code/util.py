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
            array.append(board[i][col - 1])
        return array
    
    return board[row - 1]



def get_possiblities(car, board, size):
    """
    gives all possible moves of a car in a given lane
    """

    moves = []
    row = car.row
    col = car.col

    if car.orientation == 'H':
        for i in range(1, size - 1):
            if (col + i + car.length < size and
                    board[row][col  + (i + car.length)] is None):
                moves.append(i)
            elif (col - i > -1
                    and board[row][col - i] is None):
                moves[:0] = [-i]
            else:
                break
    
    if car.orientation == 'V':
        for i in range(1, size - 1):
            if (row + i + car.length < size and
                    board[row + (i + car.length)][col] is None):
                moves.append(i)
            elif (row - i > -1
                    and board[row- i][col] is None):
                moves[:0] = [-i]
            else:
                break
        
    return moves

