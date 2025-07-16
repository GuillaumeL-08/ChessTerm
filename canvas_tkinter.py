from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint

# global vars
board_width = 1024
board_height = 1024

root = Tk()
root.title("Echecs")

img_dict = {
    'p': ImageTk.PhotoImage(Image.open('img/pion_noir.png').resize((100, 100))),
    'b': ImageTk.PhotoImage(Image.open('img/fou_noir.png').resize((100, 100))),
    'q': ImageTk.PhotoImage(Image.open('img/reine_noire.png').resize((100, 100))),
    'k': ImageTk.PhotoImage(Image.open('img/roi_noir.png').resize((100, 100))),
    'n': ImageTk.PhotoImage(Image.open('img/cavalier_noir.png').resize((100, 100))),
    'r': ImageTk.PhotoImage(Image.open('img/tour_noire.png').resize((100, 100))),
    'P': ImageTk.PhotoImage(Image.open('img/pion_blanc.png').resize((100, 100))),
    'B': ImageTk.PhotoImage(Image.open('img/fou_blanc.png').resize((100, 100))),
    'Q': ImageTk.PhotoImage(Image.open('img/reine_blanche.png').resize((100, 100))),
    'K': ImageTk.PhotoImage(Image.open('img/roi_blanc.png').resize((100, 100))),
    'N': ImageTk.PhotoImage(Image.open('img/cavalier_blanc.png').resize((100, 100))),
    'R': ImageTk.PhotoImage(Image.open('img/tour_blanche.png').resize((100, 100))),
}

# takes a col number as parameter (between 0 and 7). Returns the matching x coordinate (center of the cell) in the canvas
def get_x_from_col(col):
    if col < 0 or col > 7:
        raise ValueError(col)
    return board_width / 8 * col + board_width / 16

# takes a row number as parameter (between 0 and 7). Returns the matching x coordinate (center of the cell) in the canvas
def get_y_from_row(row):
    if row < 0 or row > 7:
        raise ValueError(row)
    return board_height / 8 * row + board_height / 16

mainframe = ttk.Frame(root)
mainframe.grid()

# display the board's borders
for i in range(8):
    label = Label(mainframe, text=chr(ord('A') + i), bg='white')
    label.grid(row=0, column=i + 1, sticky=(S))
    label = Label(mainframe, text=chr(ord('1') + i), bg='white')
    label.grid(row=i + 1, column=0, sticky=(E))

# display the moves history listbox
history_white = ["plop", "coucou", "pas mal", "mhh, peut mieux faire", "haha, raté", "ça fait quoi si on dépasse, hein?", "a", "b", "c", "d", "e", "d", "f", "g", "a"]
history_black = ["hello", "heu ok...", "j'te suis pas là", "si tu l'dis", "...", "bah ça s'affiche pas", "a", "b", "c", "d", "e", "d", "f", "g", "a"]

history_white_var = StringVar(value=history_white)
history_white_listbox = Listbox(mainframe, listvariable=history_white_var, bg="white", height=48)
history_white_listbox.grid(row=1, column=9, rowspan=8, sticky=(N))

history_black_var = StringVar(value=history_black)
history_black_listbox = Listbox(mainframe, listvariable=history_black_var, bg="white", height=48)
history_black_listbox.grid(row=1, column=10, rowspan=8, sticky=(N))

# Init chess board
canvas = Canvas(mainframe, bg="black", width=board_width, height=board_height)
canvas.grid(row=1, column=1, columnspan=8, rowspan=8)
bg_img = Image.open('img/plateau.png')
bg_photo = ImageTk.PhotoImage(bg_img)
canvas.create_image(board_width / 2, board_height / 2, image=bg_photo)

pieces_list = []

# Display one piece
def display_piece(piece, col, row):
    pieces_list.append(canvas.create_image(get_x_from_col(col), get_y_from_row(row), image=img_dict[piece]))

# Display all the pieces on the chessboard
def update_board(board):
    global canvas
    global pieces_list
    for piece in pieces_list:
        canvas.delete(piece)
    row = 0
    col = 0
    for piece in board.board_fen():
        if '1' <= piece <= '8':
            col += ord(piece) - ord('0')
        elif piece == '/':
            col = 0
            row += 1
        else:
            display_piece(piece, col, row)
            col += 1

# def delete_piece(piece):
#     canvas.delete(piece)

# def move_piece(piece, col, row):
#     delete_piece(piece)
#     return canvas.create_image(get_x_from_col(col), get_y_from_row(row), image=img_black_dict['b'])
