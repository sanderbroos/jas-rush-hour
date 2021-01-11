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



def get_possiblities(car, board):
    #alle mogelijke moves van een auto

    pass