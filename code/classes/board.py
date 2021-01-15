class Board:
    """
    Class which facilitates the playability of the game
    """
    def __init__ (self, size, cars):
        self.board = self.create_board(size,cars)
        
        
    def create_board(self, size, cars):

        board = [[None for i in range(size)] for j in range(size)]

        for car in cars.values():
            for i in range(car.length):
                if car.orientation == 'H':
                    board[car.row][car.col + i] = car
                if car.orientation == 'V':
                    board[car.row + i][car.col] = car
        return board

    def get_board(self):
        return self.board

    def set_item(self, row, col, value):
        self.board[row][col] = value