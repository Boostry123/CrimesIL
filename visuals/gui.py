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
        self.canvas = CrimeDataCanvas(self.root)

        # Configure the grid to make the canvas expandable
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        #-----------------------------------------ToolBar------------------------------------------------------------------
        self.toolBar = ToolBar(self.root,self.canvas,create_gui)
        #------------------------------------------------------------------------------------------------------------------

        

def create_gui():
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()

# Start the Tkinter loop
if __name__ == "__main__":
    create_gui()