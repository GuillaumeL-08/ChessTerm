from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint

# global vars
board_width = 1024
board_height = 1024

root = Tk()
root.title("Echecs")

img_black_dict = {
    '': ImageTk.PhotoImage(Image.open('img/pion_noir.png')),
    'F': ImageTk.PhotoImage(Image.open('img/fou_noir.png')),
    'D': ImageTk.PhotoImage(Image.open('img/reine_noire.png')),
    'R': ImageTk.PhotoImage(Image.open('img/roi_noir.png')),
    'C': ImageTk.PhotoImage(Image.open('img/cavalier_noir.png')),
    'T': ImageTk.PhotoImage(Image.open('img/tour_noire.png')),
}

img_white_dict = {
    '': ImageTk.PhotoImage(Image.open('img/pion_blanc.png')),
    'F': ImageTk.PhotoImage(Image.open('img/fou_blanc.png')),
    'D': ImageTk.PhotoImage(Image.open('img/reine_blanche.png')),
    'R': ImageTk.PhotoImage(Image.open('img/roi_blanc.png')),
    'C': ImageTk.PhotoImage(Image.open('img/cavalier_blanc.png')),
    'T': ImageTk.PhotoImage(Image.open('img/tour_blanche.png')),
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

# Display some pieces
fou1 = canvas.create_image(get_x_from_col(0), get_y_from_row(0), image=img_black_dict['F'])
fou2 = canvas.create_image(get_x_from_col(2), get_y_from_row(3), image=img_black_dict['F'])
fou3 = canvas.create_image(get_x_from_col(4), get_y_from_row(5), image=img_black_dict['F'])
fou4 = canvas.create_image(get_x_from_col(7), get_y_from_row(7), image=img_black_dict['F'])

def deletePiece(piece):
    canvas.delete(piece)

def movePiece(piece, col, row):
    deletePiece(piece)
    return canvas.create_image(get_x_from_col(col), get_y_from_row(row), image=img_black_dict['F'])

def randomMove():
    global fou2
    fou2 = movePiece(fou2, randint(0, 7), randint(0, 7))
    root.after(2000, randomMove)

# run main frame loop
root.after(2000, randomMove)
root.mainloop()
