import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from .Functions import *


# Create a class that controls the main canvas all visuals are plotted to.
class CrimeDataCanvas:
    def __init__(self, master):
        self.master = master
        self.canvas = None


    # Function to plot the top 10 cities by total crimes
    def plot_top_ten(self): 
        try:
            cities = topTen()
            city_names = [city.name[::-1] for city in cities]  # Reverse the text for Hebrew
            total_crimes = [city.total_crimes for city in cities]

            
            # Create a bar chart that supports Hebrew
            fig ,ax= plt.subplots()
            plt.rcParams['font.family'] = 'Arial'
            plt.bar(city_names, total_crimes)
            ax.set_xlabel("City", horizontalalignment='right')
            ax.set_ylabel("Total Crimes", horizontalalignment='right')
            ax.set_title("Total Crimes by City", horizontalalignment='right')
            plt.xticks(rotation=45, ha='right')
            # Check if the canvas already exists
            if self.canvas is not None:
                self.canvas.get_tk_widget().destroy()
            # Embed the plot in the Tkinter window
            self.canvas = FigureCanvasTkAgg(fig, master=self.master)
            self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=11, padx=10, pady=10, sticky="nsew")
            self.canvas.draw()
          
            
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")

    # Function to plot the top 5 cities by total crimes
    def plot_top_five(self): 
        try:
            cities = topFive()
            city_names = [city.name[::-1] for city in cities]  # Reverse the text for Hebrew
            total_crimes = [city.total_crimes for city in cities]

            
            # Create a bar chart that supports Hebrew
            fig ,ax= plt.subplots()
            plt.rcParams['font.family'] = 'Arial'
            plt.bar(city_names, total_crimes)
            ax.set_xlabel("City", horizontalalignment='right')
            ax.set_ylabel("Total Crimes", horizontalalignment='right')
            ax.set_title("Total Crimes by City", horizontalalignment='right')
            plt.xticks(rotation=45, ha='right')
            # Check if the canvas already exists
            if self.canvas is not None:
                self.canvas.get_tk_widget().destroy()
            # Embed the plot in the Tkinter window
            self.canvas = FigureCanvasTkAgg(fig, master=self.master)
            self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=11, padx=10, pady=10, sticky="nsew")
            self.canvas.draw()
          
            
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")

