from chess import *
from canvas_tkinter import *

board = Board()

board.push_san('Nf3')

update_board(board)

root.mainloop()
