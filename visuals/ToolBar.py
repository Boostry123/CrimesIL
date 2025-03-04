import tkinter as tk
from tkinter.ttk import *

from .Functions.Functionality import *
from .main_canvas import *


#The toolbar recives the root (TK window), 
# main_canvas (the canvas plots are displayed), 
# create_gui (function to create a new GUI)
class ToolBar:
    def __init__(self, root,main_canvas,create_gui):
        self.root = root
        self.canvas = main_canvas
    
        #-----------------------------------------Buttons------------------------------------------------------------------
        style = Style()
        style.configure("TButton", font=("Arial", 10))

        # Button for adding an app

        self.addApp = Button(self.root, text="Add", command=create_gui, style="TButton")
        self.addApp.grid(row=0, column=2,sticky="en")
                

        # Button for the top 10 cities
                
        plot_Top10_button = Button(self.root, text="Top 10", command=self.canvas.plot_top_ten, style="TButton")
        plot_Top10_button.grid(row=0, column=0, padx=10,sticky="nsew")

        #button for the top 5 cities

        plot_Top5_button = Button(self.root, text="Top 5", command=self.canvas.plot_top_five, style="TButton")
        plot_Top5_button.grid(row=0, column=1, padx=10,sticky="nsew")
            
        #------------------------------------------------------------------------------------------------------------------
