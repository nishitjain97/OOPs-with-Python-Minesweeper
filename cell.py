from tkinter import Button
from tkinter import Label
import ctypes
import random
import settings
import os

class Cell:
    all = []
    cell_count_label_object = None
    cell_count = settings.CELL_COUNT

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=settings.WIDTH // 333,
            height=settings.HEIGHT // 300,
            highlightbackground="#22303C",
            fg="black"
        )

        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-2>', self.right_click_actions)

        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left: {Cell.cell_count}",
            width=12,
            height=4,
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine_candidate:
            return

        if self.is_mine:
            self.show_mine()
        else:
            if self.count_mines_surrounded == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

            if Cell.cell_count == settings.MINES_COUNT:
                os.system("osascript -e 'Tell application \"System Events\" to display dialog \"You have located all mines!\" with title \"Game won!!\"'")
                quit()

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on x and y values
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]

        return cells

    @property
    def count_mines_surrounded(self):
        counter = 0

        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1

        self.cell_btn_object.configure(
            text=self.count_mines_surrounded
        )

        # Replace text of cell_count_label with new count
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.configure(
                text=f"Cells Left: {Cell.cell_count}"
            )

        self.is_open = True

    def show_mine(self):
        # A logic to interrupt game for player lost!
        os.system("osascript -e 'Tell application \"System Events\" to display dialog \"You clicked a mine!\" with title \"Game lost!!\"'")
        quit()

    def right_click_actions(self, event):
        if self.is_open:
            return

        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                highlightbackground="orange"
            )

            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                highlightbackground="#22303C"
            )
            
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        mine_list = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        
        for cell in mine_list:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"