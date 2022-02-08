from tkinter import Button
class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
    
    def create_btn_object(self, location):
        btn = Button(
            location,
            text='text'
        )
        # left click
        btn.bind('<Button-1>', self.left_click_actions) # event trigger, DON"T call the method, just pass it as a reference
        # right click
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn
    
    def left_click_actions(self, event):
        print(event)
        print('I am left clicked')
        
    def right_click_actions(self, event):
        print(event)
        print('I am right clicked')