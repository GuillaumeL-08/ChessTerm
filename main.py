from chess import *
from canvas_tkinter import *

board = Board()

board.push_san('Nf3')

update_board(board)

update_history_black('nf5')

update_history_white('Nf3')

root.mainloop()
