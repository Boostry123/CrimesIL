import tkinter as tk
from tkinter.ttk import *
import matplotlib.pyplot as plt

from .main_canvas import CrimeDataCanvas

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
        #-----------------------------------------Buttons------------------------------------------------------------------
        style = Style()
        style.configure("TButton", font=("Arial", 10))
        self.addApp = Button(self.root, text="Add", command=create_gui)
        self.addApp.grid(row=0, column=2,sticky="en")
        

        # Button for the top 10 cities
        
        plot_Top10_button = Button(self.root, text="Top 10", command=self.canvas.plot_top_ten)
        plot_Top10_button.grid(row=0, column=0, padx=10,sticky="nsew")

        #button for the top 5 cities

        plot_Top5_button = Button(self.root, text="Top 5", command=self.canvas.plot_top_five)
        plot_Top5_button.grid(row=0, column=1, padx=10,sticky="nsew")
       
        #------------------------------------------------------------------------------------------------------------------

        

def create_gui():
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()

# Start the Tkinter loop
if __name__ == "__main__":
    create_gui()