# Package import
from ctypes import util
from tkinter import *

from numpy import left_shift
import settings
import utility
from cell import Cell

# Initialize our window
root = Tk()

# Override settings of window
# Configure colors for our window
root.configure(bg="#181818")

# Change title
root.title("Minesweeper Game!")

# Disallow resizing of window
root.resizable(False, False)

# Change size of window
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")

# Create frame for header
header_frame = Frame(
    root,
    bg="#282828",
    width=settings.WIDTH,
    height=utility.height_prct(25)
)
header_frame.place(x=0, y=0)

game_title = Label(
    header_frame,
    fg="#8899A6",
    bg="#282828",
    text="Minesweeper Game",
    font=('', 48)
)

game_title.place(
    x=utility.width_prct(30),
    y=0
)

# Frame for scores
sidebar_frame = Frame(
    root,
    bg="#181818",
    width=utility.width_prct(25),
    height=settings.HEIGHT - utility.height_prct(25)
)
sidebar_frame.place(x=0, y=utility.height_prct(25))

# Main frame for game
center_frame = Frame(
    root,
    bg="#181818",
    height=utility.height_prct(75),
    width=utility.width_prct(75)
)
center_frame.place(
    x=utility.width_prct(25), 
    y=utility.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Call label from Cell class
Cell.create_cell_count_label(sidebar_frame)
Cell.cell_count_label_object.place(
    x = utility.width_prct(3),
    y = utility.height_prct(18)
)

Cell.randomize_mines()

# To keep window active
root.mainloop()