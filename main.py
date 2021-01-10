from code.classes.board import Board
from code.util import search_board, get_position, get_lane

if __name__ == "__main__":
    board = Board(6, "data/Rushhour6x6_1.csv")
    board.draw_board()


print()
print(board.board[0][1])
print()
print(get_lane('A', 'V', board.board))

