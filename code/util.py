from random import choice

def get_lane(car, board):
    """
    Gets whole row/col in which the car/truck is located.
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
        if i > 0 and move[0] == moves[i-1][0]:
            move[1] += moves.pop(i-1)[1]
            i -= 1

        i += 1

    return [move for move in moves if move[1] != 0]


def output(moves):
    """
    Cleans and saves the made moves to an output file
    """
    moves = clean_moves(moves)

    output_string = "car,move"
    for move in moves:
        output_string += f'\n{move[0]},{move[1]}'

    solution = open("docs/output.csv", "w")
    solution.write(output_string)
    solution.close()


def random_move_quick(game):
    move = None
    while not move:
        car = choice(list(game.cars.values()))
        moves = get_possiblities(car, game.board.get_board())
        # print(moves)
        if moves:
            move = [car.name, choice(moves)]

    return move
