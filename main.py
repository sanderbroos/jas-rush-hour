from code.classes import board

if __name__ == "__main__":
    # use command line araguments?
    board = board.Board(6, "data/Rushhour6x6_1.csv")
    board.draw_board()