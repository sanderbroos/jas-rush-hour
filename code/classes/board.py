class Board:
    """
    Represents the board of a game.
    """
    def __init__(self, size, cars):
        self.board = self.create_board(size,cars)
    

    def __str__(self):
        """
        Creates a string representation of the board.
        """
        string = ''
        for row in self.board:
            for item in row:
                if item == None:
                    string += "_ "
                else:
                    string += f"{item.name:<2}"
            string += '\n'
        
        return string
        
        
    def create_board(self, size, cars):
        """
        Initializes the board with its cars.
        """
        board = [[None for i in range(size)] for j in range(size)]

        for car in cars.values():
            for i in range(car.length):
                if car.orientation == 'H':
                    board[car.row][car.col + i] = car
                if car.orientation == 'V':
                    board[car.row + i][car.col] = car

        return board


    def get_board(self):
        """
        Returns the board.
        """
        return self.board


    def get_size(self):
        """
        Returns the size of the board.
        """
        return len(self.board)


    def set_item(self, row, col, value):
        """
        Implements a move by changing car placement.
        """
        self.board[row][col] = value