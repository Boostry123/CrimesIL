from tkinter import *
from tkinter.ttk import *

from .main_canvas import CrimeDataCanvas
class MainPage:
    def __init__(self, gui):
        self.gui = gui

        self.main_page_frame = Frame(self.gui)
        self.main_page_frame.grid_rowconfigure(2, weight=1)
        for i in range(4):
            self.main_page_frame.grid_columnconfigure(i, weight=1)
        self.main_page_frame.grid(row=2,column=0, columnspan=4, sticky="nsew")
        
    def  buttons(self):
        print("buttons")
        #-----------------------------------------Label----------------------------------------------------------------
        label = Label(self.main_page_frame, text="Welcome to the Crime Data Visualization Tool", font=("Arial", 20))
        label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        #----------------------------buttons------------------------------------------------------------------
        north = Button(self.main_page_frame, text="North", command=..., style="TButton")
        north.grid(row=2, column=0,columnspan=3, padx=40, pady=20, sticky="nsew")

        center = Button(self.main_page_frame, text="Center", command=..., style="TButton")
        center.grid(row=3, column=0,columnspan=3, padx=40, pady=20, sticky="nsew")

        negev = Button(self.main_page_frame, text="Negev", command=..., style="TButton")
        negev.grid(row=4, column=0,columnspan=3, padx=40, pady=20, sticky="nsew")

        #---------------------------------------------------------------------------------------------------------
    def northCities():
        ...

    def hide(self):
        if(self.main_page_frame.winfo_viewable()):
            self.main_page_frame.grid_forget()
    def show(self):
        if(not self.main_page_frame.winfo_viewable()):
            self.main_page_frame.grid()