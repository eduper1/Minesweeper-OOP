from select import select
from tkinter import Button
import random
import settings


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append all objects in Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f'{self.x}, {self.y}'
        )
        # left click
        # event trigger, DON"T call the method, just pass it as a reference
        btn.bind('<Button-1>', self.left_click_actions)
        # right click
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        # return a cell object based on values: x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1), 
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property    
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter
    
    def show_cell(self):
        print(self.surrounded_cells_mines_length)

    def show_mine(self):
        # a logic to interrupt the game and display a message that the player lost
        self.cell_btn_object.configure(
            bg="red"
        )

    def right_click_actions(self, event):
        print(event)
        print('I am right clicked')

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
