from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

board_width = 1024
board_height = 1024

def get_x_from_col(col):
    return board_width / 8 * col + board_width / 16

def get_y_from_row(row):
    return board_height / 8 * row + board_height / 16

root = Tk()
root.title("Echecs")

mainframe = ttk.Frame(root)
mainframe.grid()

canvas = Canvas(mainframe, bg="black", width=board_width, height=board_height)
canvas.pack()

for i in range(8):
    mainframe.rowconfigure(i, minsize=128)
    mainframe.columnconfigure(i, minsize=128)

# Init chess board
bg_img = Image.open('img/plateau.png')
bg_photo = ImageTk.PhotoImage(bg_img)
canvas.create_image(board_width / 2, board_height / 2, image=bg_photo)

fou_img = Image.open("img/Chess_bdt60.png")
fou_photo = ImageTk.PhotoImage(fou_img)
canvas.create_image(get_x_from_col(0), get_y_from_row(0), image=fou_photo)
canvas.create_image(get_x_from_col(2), get_y_from_row(3), image=fou_photo)
canvas.create_image(get_x_from_col(4), get_y_from_row(5), image=fou_photo)
canvas.create_image(get_x_from_col(7), get_y_from_row(7), image=fou_photo)

# run main frame loop
root.mainloop()
