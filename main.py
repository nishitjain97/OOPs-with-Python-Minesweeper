# Package import
from ctypes import util
from tkinter import *
import settings
import utility

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

# Frame for scores
sidebar_frame = Frame(
    root,
    bg="#404040",
    width=utility.width_prct(25),
    height=settings.HEIGHT - utility.height_prct(25)
)
sidebar_frame.place(x=0, y=utility.height_prct(25))

# Main frame for game
center_frame = Frame(
    root,
    bg="#B3B3B3",
    height=utility.height_prct(75),
    width=utility.width_prct(75)
)
center_frame.place(x=utility.width_prct(25), y=utility.height_prct(25))

# To keep window active
root.mainloop()