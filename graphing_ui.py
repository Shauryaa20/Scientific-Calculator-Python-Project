# graphing_ui.py
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import re

class GraphingUI:
    def __init__(self, window, theme):
        self.window = window
        self.theme = theme
        self.window.title("Function Graphing")
        self.window.geometry("1000x600")
        
        # Create main container
        self.main_container = ttk.Frame(window, padding=10)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create left panel for input
        self.create_input_panel()
        
        # Create right panel for graph
        self.create_graph_panel()
        
        # Initialize the plot
        self.initialize_plot()
    
    def create_input_panel(self):
        input_frame = ttk.LabelFrame(self.main_container, text="Graph Settings", padding=10)
        input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        # Function input
        ttk.Label(input_frame, text="Function:").pack(anchor=tk.W, pady=(0, 5))
        self.function_var = tk.StringVar(value="x**2")
        self.function_entry = ttk.Entry(input_frame, textvariable=self.function_var, width=30)
        self.function_entry.pack(fill=tk.X, pady=(0, 10))
        
        # Range inputs
        range_frame = ttk.Frame(input_frame)
        range_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(range_frame, text="X Range:").grid(row=0, column=0, sticky=tk.W)
        self.x_min = ttk.Entry(range_frame, width=8)
        self.x_min.insert(0, "-10")
        self.x_min.grid(row=0, column=1, padx=5)
        ttk.Label(range_frame, text="to").grid(row=0, column=2)
        self.x_max = ttk.Entry(range_frame, width=8)
        self.x_max.insert(0, "10")
        self.x_max.grid(row=0, column=3, padx=5)
        
        # Plot style options
        style_frame = ttk.LabelFrame(input_frame, text="Plot Style", padding=10)
        style_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(style_frame, text="Color:").pack(anchor=tk.W)
        self.color_var = tk.StringVar(value="blue")
        color_options = ['blue', 'red', 'green', 'purple', 'orange']
        color_menu = ttk.OptionMenu(style_frame, self.color_var, *color_options)
        color_menu.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(style_frame, text="Line Style:").pack(anchor=tk.W)
        self.line_style_var = tk.StringVar(value="-")
        style_options = [('-', 'Solid'), ('--', 'Dashed'), (':', 'Dotted')]
        self.line_style_var.set(style_options[0][0])
        style_menu = ttk.OptionMenu(style_frame, self.line_style_var,
                                  *[style[0] for style in style_options])
        style_menu.pack(fill=tk.X, pady=(0, 5))
        
        # Grid options
        grid_frame = ttk.LabelFrame(input_frame, text="Grid Options", padding=10)
        grid_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.show_grid = tk.BooleanVar(value=True)
        ttk.Checkbutton(grid_frame, text="Show Grid",
                       variable=self.show_grid,
                       command=self.update_plot).pack(anchor=tk.W)
        
        self.show_axes = tk.BooleanVar(value=True)
        ttk.Checkbutton(grid_frame, text="Show Axes",
                       variable=self.show_axes,
                       command=self.update_plot).pack(anchor=tk.W)
        
        # Buttons
        button_frame = ttk.Frame(input_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Plot", command=self.update_plot).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_plot).pack(side=tk.LEFT, padx=5)
    
    def create_graph_panel(self):
        self.graph_frame = ttk.LabelFrame(self.main_container, text="Graph", padding=10)
        self.graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    def initialize_plot(self):
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        # Create canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Initialize empty plot
        self.update_plot()
    
    def parse_function(self, func_str):
        # Replace ^ with ** for exponentiation
        func_str = func_str.replace('^', '**')
        
        # Define allowed mathematical functions
        safe_dict = {
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'exp': np.exp,
            'log': np.log,
            'sqrt': np.sqrt,
            'pi': np.pi,
            'e': np.e,
            'abs': np.abs,
            'x': None  # Will be replaced with actual x values
        }
        
        # Check for invalid characters
        if not re.match(r'^[0-9x+\-*/()., \w]+$', func_str):
            raise ValueError("Invalid characters in function")
        
        try:
            # Create lambda function that will use numpy arrays
            def func(x):
                safe_dict['x'] = x  # Set x to the numpy array
                return eval(func_str, {"__builtins__": None}, safe_dict)
            return func
        except:
            raise ValueError("Invalid function expression")
    
    def update_plot(self):
        try:
            # Clear current plot
            self.ax.clear()
            
            # Get x range
            x_min = float(self.x_min.get())
            x_max = float(self.x_max.get())
            
            # Generate x values
            x = np.linspace(x_min, x_max, 1000)
            
            # Parse and evaluate function
            func = self.parse_function(self.function_var.get())
            y = func(x)
            
            # Plot function
            self.ax.plot(x, y, color=self.color_var.get(),
                        linestyle=self.line_style_var.get(),
                        label=self.function_var.get())
            
            # Set grid
            self.ax.grid(self.show_grid.get())
            
            # Show/hide axes
            if self.show_axes.get():
                self.ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
                self.ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
            
            # Add legend
            self.ax.legend()
            
            # Update canvas
            self.canvas.draw()
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Error plotting function: {str(e)}")
    
    def clear_plot(self):
        self.ax.clear()
        self.ax.grid(self.show_grid.get())
        if self.show_axes.get():
            self.ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            self.ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        self.canvas.draw()