from random import choice


def get_lane(car, board):
    """
    Gets whole row/col in which the car/truck is located.
    """
    if car.orientation == 'V':
        return [row[car.col] for row in board]
    
    return board[car.row]


def get_possibilities(car, board):
    """
    Gives all possible moves of a car in a given lane.
    """
    moves = []
    size = len(board)
    lane = get_lane(car, board)

    if car.orientation == 'H':
        index = car.col
    elif car.orientation == 'V':
        index = car.row

    # add valid moves in the forward direction
    for i in range(1, size - 1):
        # if the car isn't out of the board and this space is unoccupied
        if (index + i + car.length <= size and
                lane[index + (i + car.length) - 1] == None):
            moves.append(i)
        # if the car can't go this far, it also can't go further
        else:
            break
    
    # add valid moves in the backward direction
    for i in range(1, size - 1): 
        # if the car isn't out of the board and this space is unoccupied
        if (index - i >= 0
                and lane[index - i] == None):
            moves.append(-i)
        # if the car can't go this far, it also can't go further
        else:
            break
        
    return moves


def all_moves(game):
    """
    Returns list with all possible moves for all cars
    like [[car1,move1], [car1,move2], etc].
    """
    moves = []
    cars = game.cars
    board = game.board.get_board()

    for car in cars.keys():
        possibilities = get_possibilities(cars.get(car), board)

        for move in possibilities:
            moves.append([car, move])

    return moves


def clean_moves(moves):
    """
    Combines consecutive moves by the same car into one move.
    Removes moves where a car moves 0 spots.
    """
    i = 0

    while i < len(moves):
        move = moves[i]
        
        # if one car makes two moves directly after each other, combine 
        # these moves into 1
        if i > 0 and move[0] == moves[i-1][0]:
            move[1] += moves.pop(i-1)[1]
            i -= 1

        i += 1

    return [move for move in moves if move[1] != 0]


def output(moves):
    """
    Cleans and saves the made moves to an output file.
    """
    output_string = "car,move"
    for move in clean_moves(moves):
        output_string += f'\n{move[0]},{move[1]}'

    output_file = open("docs/output.csv", "w")
    output_file.write(output_string)
    output_file.close()


def random_move_quick(game):
    """
    Returns a random move by first choosing a car, then a move for that car.
    This function is much faster than choosing from all_moves, but here not all 
    moves have the same probability of being chosen, so less "true" random.
    """
    move = None
    while not move:
        car = choice(list(game.cars.values()))
        moves = get_possibilities(car, game.board.get_board())
        
        if moves:
            move = [car.name, choice(moves)]

    return move


def direction_to_int(direction):
    """
    Converts a direction to an integer, if it's not already one.
    Returns False if not possible.
    """
    if (type(direction) == int or direction.isdigit() or 
       direction[0] == '-' and direction[1:].isdigit()):
        return int(direction)
    
    return False