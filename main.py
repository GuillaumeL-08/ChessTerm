from tkinter import *
from tkinter import ttk
from tksvg import SvgImage

root = Tk()
root.title("Echecs")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# board = [
#     ['T', 'C', 'F', 'R', 'D', 'F', 'C', 'T'],
#     ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
#     ['', '', '', '', '', '', '', ''],
#     ['', '', '', '', '', '', '', ''],
#     ['', '', '', '', '', '', '', ''],
#     ['', '', '', '', '', '', '', ''],
#     ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
#     ['T', 'C', 'F', 'R', 'D', 'F', 'C', 'T'],
# ]

# Init chess board
board_frame = ttk.Frame(mainframe, width=400, height=400)
board_frame.grid(column=0, row=0, columnspan=8, rowspan=8)

board_frame.background_image = PhotoImage(file='img/ChessBoard110.png')
board_frame.background_image.resize
background = Label(board_frame, image=board_frame.background_image)
board_frame.background = background
board_frame.background.pack(fill=BOTH, expand=YES)
background.place(x=0, y=0, relwidth=1, relheight=1)

# red_cell = ttk.Style()
# red_cell.configure('Red.TFrame', background='red')
# black_cell = ttk.Style()
# black_cell.configure('Blue.TFrame', background='blue')
# board_cells = []
# use_red = True
# for col in range(8):
#     board_cells.append([])
#     for row in range(8):
#         cell_frame = ttk.Frame(board_frame, style=('Red.TFrame' if use_red else 'Blue.TFrame'), width=50, height=50)
#         cell_frame.grid(column=col, row=row)
#         board_cells[col].append(cell_frame)
#         use_red = not use_red
#     use_red = not use_red

piece_image = PhotoImage(file='img/Chess_bdt60.png')

# def get_image(piece, color):
#     return piece_image

# def display_piece(piece, color, row, col):
    # img = Label(board_cells[col][row], image=get_image(piece, color))
# piece = Label(board_frame, image=piece_image)
# piece.grid(column=2, row=3)

# display_piece('F', 'white', 2, 3)

# run main frame loop
root.mainloop()
