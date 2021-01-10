def search_board(car,board):
    """
    finds first coordinaat of car/truck (like a pointer).
    """

    for x_cor,y_cor in enumerate(board):
        try:
            return [x_cor, y_cor.index(car)]
        except ValueError:
            pass
    
    raise ValueError(f'{car} is invalid input')


def get_lane(car, orientation, board):
    """
    Gets whole row/col in which the car/truck is located.
    Makes is_valid function easier to read
    """

    location = search_board(car,board)
    row = location[0]
    col = location[1]
    array = []

    if orientation == 'V':
        for i in range(0,len(board)):
            array.append(board[i][col])
        return array
    
    return board[row]


def empty_lane(location, move, lane):
    """
    checks if no traffic is blocking the move. Makes is_valid function more readable.
    """
    
    # check direction left/right = up/down
    if move > 1:
        pass



def get_position(car, coordinaat, orientation, length):
    """
    returns the location of a car/truck as a list of
    coordinaats [x,[y1,y2]] depending on orientation


    een car object is hier wel handig voor lengte en orientation 
    scheelt input waardes

    deze functie mogelijk niet nodig
    """
    colposition = coordinaat[1]
    rowposition = coordinaat[0]
    
    if orientation == "H":
        colposition = [colposition + i for i in range(0, length)]
        position = [rowposition, colposition]
        return position
    
    rowposition = [rowposition + i for i in range(0, length)]
    position = [rowposition, colposition]
    return position