import tkinter as tk
from tkinter.ttk import *
import matplotlib.pyplot as plt

from .main_canvas import CrimeDataCanvas
from .ToolBar import *
from .Functions import *

# Create a class to handle the GUI
class Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Crime Data Visualization")
        self.root.geometry("800x600")

        # Main canvas the plot will be displayed on
        main_canvas_frame = Frame(self.root)
        main_canvas_frame.grid_rowconfigure(1, weight=1)
        main_canvas_frame.grid_columnconfigure(0, weight=1)
        main_canvas_frame.grid(row=1,column=0, columnspan=3, sticky="nsew")
        self.canvas = CrimeDataCanvas(main_canvas_frame)

        # Configure the grid to make the canvas expandable
        self.root.grid_rowconfigure(1, weight=1)
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)

        #-----------------------------------------ToolBar------------------------------------------------------------------
        toolBar_frame = Frame(self.root,border=1,relief="solid")

        toolBar_frame.grid_rowconfigure(0, weight=1)
        toolBar_frame.grid_columnconfigure(2, weight=1)

        toolBar_frame.grid(row=0,column=0,columnspan=3, sticky="ew")
        self.toolBar = ToolBar(toolBar_frame, self.canvas, create_gui)
        
        #------------------------------------------------------------------------------------------------------------------

        #-----------------------------------------Main---------------------------------------------------------------------

        
        

def create_gui():
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()

# Start the Tkinter loop
if __name__ == "__main__":
    create_gui()