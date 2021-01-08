from code.classes.board import Board

if __name__ == "__main__":
    # use command line arguments to retrieve to be used csv?
    board = board.Board(6, "data/Rushhour6x6_1.csv")
    board.draw_board()