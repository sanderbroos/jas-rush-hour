def get_lane(car, board):
    """
    Gets whole row/col in which the car/truck is located.
    Makes is_valid function easier to read.
    """

    if car.orientation == 'V':
        return [row[car.col] for row in board]
    
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
    elif car.orientation == 'V':
        index = car.row

    for i in range(1, size - 1):
        if (index + i + car.length <= size and
                lane[index + (i + car.length) - 1] == None):
            moves.append(i)
        else:
            break
    
    for i in range(1, size - 1): 
        if (index - i >= 0
                and lane[index - i] == None):
            moves.append(-i)
        else:
            break
        
    return moves

def all_moves(game):
    """ Returns list with all possible moves for all cars 
    like [[car1,move1], [car1,move2], etc]"""
    
    moves = []
    cars = game.cars
    board = game.board.get_board()

    for car in cars.keys():
        possibilities = get_possiblities(cars.get(car), board)

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

def all_movesv1(cars, board):
    """ Returns list with all possible moves for all cars 
    like [[car1,move1], [car1,move2], etc]"""
    
    moves = []
    for car in cars.values():
        possibilities = get_possiblities(car, board)

        for move in possibilities:
            moves.append([car, move])

    return moves

# want to find a way to check valid moves without using all of game or board, try to use dict
def valid_moves(cars, size):
    # loop every car and every square car can move to in empty board
    # check if 'new direction' already has car on it 
    # (car.orientation to determine car.col or car.row and car.length to determine square occupied)
    # if not occupied add move to list of moves
    moves = []

    for car in cars:
        current_car = cars.get(car)
        # buggy, most likely appending wrong direction to moves, currenlty searches outside the board
        # what happens if a car is in between the current car and direction to a free place?
        for direction in range ((-size + 2), (size - 2)):
            occupied = False
            if current_car.orientation == 'V':
                for length in range (current_car.length - 1):
                    # will append before checkin whole car length
                    if  is_occupied(cars, current_car.col + length + direction, current_car.orientation):
                        occupied = True
                if occupied == False:
                    moves.append([current_car, direction])

            else:
                for length in range (current_car.length - 1):
                    if  is_occupied(cars, current_car.row + length + direction, current_car.orientation):
                        occupied = True
                if occupied == False:
                    moves.append([current_car, direction])
    print(moves)
    return moves

def is_occupied(cars, place, orientation):
    # can i fit this into valid_moves?
    for car in cars:
        current_car = cars.get(car)
        if current_car.orientation == 'V':
            if place == current_car.col:
                return True
        if current_car.orientation == 'H':
            if place == current_car.row:
                return True
        
    return False