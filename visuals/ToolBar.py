import tkinter as tk
from tkinter.ttk import *

from .Functions.Functionality import *
from .main_canvas import *
from .main_page import *


#The toolbar recives the root (TK window), 
# main_canvas (the canvas plots are displayed), 
# create_gui (function to create a new GUI)
class ToolBar:
    def __init__(self, frame,main_canvas,main_page,create_gui):
        self.root = frame
        self.canvas = main_canvas
        self.page = main_page
    
        #-----------------------------------------Label--------------------------------------------------------------------

        # Label for the quick actions
        label = Label(self.root, text="Quick Actions:")
        label.grid(row=0, column=0, padx=10,sticky="w")

        #-----------------------------------------Buttons------------------------------------------------------------------
        style = Style()
        style.configure("TButton", font=("Arial", 10))


        # Button for adding an app

        self.addApp = Button(self.root, text="Add", command=create_gui, style="TButton")
        self.addApp.grid(row=0, column=4,sticky="en")
                
        # Button for the top 10 cities
                
        self.plot_Top10_button = Button(self.root, text="Top 10", command=lambda : [self.page.hide(), self.canvas.plot_top_ten(),self.canvas.show()], style="TButton")
        self.plot_Top10_button.grid(row=0, column=3, padx=10,sticky="nsew")

        #button for the top 5 cities

        self.plot_Top5_button = Button(self.root, text="Top 5", command=lambda : [self.page.hide(), self.canvas.plot_top_five(),self.canvas.show()], style="TButton")
        self.plot_Top5_button.grid(row=0, column=2, padx=10,sticky="nsew")
            
        #button for Home

        self.home = Button(self.root, text="Home", command=lambda : [self.page.show(), self.canvas.hide()], style="TButton")
        self.home.grid(row=0, column=0, padx=10,sticky="nsew")
        #------------------------------------------------------------------------------------------------------------------
