from ctypes import util
from tkinter import *

from matplotlib.pyplot import text
from cell import Cell
import settings
import Utils

root = Tk()

# Over ride the settings of the windows
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

# create top frame
top_frame = Frame(
    root,
    bg='red', # Change later to black
    width=settings.WIDTH,
    height= Utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    text="FAIZA GAME",
    bg='red',
    fg="White",
    font=('serrif', 28)
)
game_title.place(
    x=Utils.width_prct(40),
    y=Utils.height_prct(8)
)
# create left frame
left_frame = Frame(
    root,
    bg='yellow', # Change  latter to black
    width=Utils.width_prct(25),
    height=Utils.height_prct(75)
)
left_frame.place(x=0, y=Utils.height_prct(25))

# create center frame
center_frame = Frame(
    root,
    bg='Pink',
    width=Utils.width_prct(75),
    height=Utils.height_prct(75)
)
center_frame.place(x=Utils.width_prct(25), y=Utils.height_prct(25))

for x in range(settings.GRID_SIZE): #0,1,2,3,4
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            row=y,
            column=x
        )
   
# call the label fromCell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.place(
    x=0,
    y=0
)
        
Cell.randomize_mines()
# for c in Cell.all:
#     print(c.is_mine)

# Run the window
root.mainloop()