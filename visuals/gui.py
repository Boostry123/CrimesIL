import tkinter as tk
from tkinter.ttk import *
import matplotlib.pyplot as plt

from .main_canvas import CrimeDataCanvas
from .ToolBar import *
from .Functions import *
from .main_page import *

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
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        #-----------------------------------------Main---------------------------------------------------------------------
        self.mainPage = MainPage(self.root)
        self.mainPage.buttons()

        #-----------------------------------------ToolBar------------------------------------------------------------------
        toolBar_frame = Frame(self.root,border=1,relief="solid")

        toolBar_frame.grid_rowconfigure(0, weight=1)
        toolBar_frame.grid_columnconfigure(4, weight=1)

        toolBar_frame.grid(row=0,column=0,columnspan=4, sticky="ew")
        self.toolBar = ToolBar(toolBar_frame, self.canvas,self.mainPage, create_gui)
        
        #------------------------------------------------------------------------------------------------------------------

        
        
        

def create_gui():
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()

# Start the Tkinter loop
if __name__ == "__main__":
    create_gui()