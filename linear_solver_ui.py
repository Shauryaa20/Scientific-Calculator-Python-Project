# linear_solver_ui.py
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from linear_solver_utils import solve_linear_system
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class LinearSolverUI:
    def __init__(self, window, theme):
        self.window = window
        self.theme = theme
        self.window.title("Linear Equation Solver")
        self.window.geometry("800x600")
        
        # Main container
        self.main_frame = ttk.Frame(window, padding=10, style='Solver.TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configure styles
        self.configure_styles()
        
        # Create main interface
        self.create_interface()
    
    def configure_styles(self):
        style = ttk.Style()
        style.configure('Solver.TFrame', padding=10)
        style.configure('Result.TLabel', font=('Helvetica', 12))
    
    def create_interface(self):
        # Input frame
        input_frame = ttk.LabelFrame(self.main_frame, text="Enter Coefficients", padding=10)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # First equation
        eq1_frame = ttk.Frame(input_frame)
        eq1_frame.pack(fill=tk.X, pady=5)
        
        self.a1 = ttk.Entry(eq1_frame, width=5)
        self.a1.pack(side=tk.LEFT, padx=2)
        ttk.Label(eq1_frame, text="x +").pack(side=tk.LEFT, padx=2)
        self.b1 = ttk.Entry(eq1_frame, width=5)
        self.b1.pack(side=tk.LEFT, padx=2)
        ttk.Label(eq1_frame, text="y =").pack(side=tk.LEFT, padx=2)
        self.c1 = ttk.Entry(eq1_frame, width=5)
        self.c1.pack(side=tk.LEFT, padx=2)
        
        # Second equation
        eq2_frame = ttk.Frame(input_frame)
        eq2_frame.pack(fill=tk.X, pady=5)
        
        self.a2 = ttk.Entry(eq2_frame, width=5)
        self.a2.pack(side=tk.LEFT, padx=2)
        ttk.Label(eq2_frame, text="x +").pack(side=tk.LEFT, padx=2)
        self.b2 = ttk.Entry(eq2_frame, width=5)
        self.b2.pack(side=tk.LEFT, padx=2)
        ttk.Label(eq2_frame, text="y =").pack(side=tk.LEFT, padx=2)
        self.c2 = ttk.Entry(eq2_frame, width=5)
        self.c2.pack(side=tk.LEFT, padx=2)
        
        # Buttons frame
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(button_frame, text="Solve", command=self.solve_2var).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_2var).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Plot", command=self.plot_2var).pack(side=tk.LEFT, padx=5)
        
        # Result frame
        self.result_frame = ttk.LabelFrame(self.main_frame, text="Results", padding=10)
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.result_label = ttk.Label(self.result_frame, text="", style='Result.TLabel')
        self.result_label.pack()
        
        # Create figure for plotting
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.result_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def solve_2var(self):
        try:
            coefficients = [
                [float(self.a1.get()), float(self.b1.get()), float(self.c1.get())],
                [float(self.a2.get()), float(self.b2.get()), float(self.c2.get())]
            ]
            solution = solve_linear_system(coefficients)
            self.result_label.config(
                text=f"Solution:\nx = {solution[0]:.4f}\ny = {solution[1]:.4f}"
            )
            self.plot_2var()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def clear_2var(self):
        for entry in [self.a1, self.b1, self.c1, self.a2, self.b2, self.c2]:
            entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.ax.clear()
        self.canvas.draw()
    
    def plot_2var(self):
        try:
            # Get coefficients
            a1, b1, c1 = float(self.a1.get()), float(self.b1.get()), float(self.c1.get())
            a2, b2, c2 = float(self.a2.get()), float(self.b2.get()), float(self.c2.get())
            
            # Create x and y values
            x = np.linspace(-100, 100, 1000)
            
            # Clear previous plot
            self.ax.clear()
            
            # Plot first equation
            if a1 == 0 and b1 != 0:  # Horizontal line
                y1 = c1/b1
                self.ax.axhline(y=y1, label='Equation 1')
            elif b1 == 0 and a1 != 0:  # Vertical line
                x1 = c1/a1
                self.ax.axvline(x=x1, label='Equation 1')
            else:  # Regular line
                y1 = (-a1*x + c1) / b1
                self.ax.plot(x, y1, label='Equation 1')
                
            # Plot second equation
            if a2 == 0 and b2 != 0:  # Horizontal line
                y2 = c2/b2
                self.ax.axhline(y=y2, color='g', label='Equation 2')
            elif b2 == 0 and a2 != 0:  # Vertical line
                x2 = c2/a2
                self.ax.axvline(x=x2, color='g', label='Equation 2')
            else:  # Regular line
                y2 = (-a2*x + c2) / b2
                self.ax.plot(x, y2, color='g', label='Equation 2')
            
            # Add grid and labels
            self.ax.grid(True)
            self.ax.set_xlabel('x')
            self.ax.legend()
            
            # Set reasonable limits
            self.ax.set_xlim(-100, 100)
            self.ax.set_ylim(-100, 100)
            
            # Add origin lines
            self.ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            self.ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
            
            # Update canvas
            self.canvas.draw()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error plotting equations: {str(e)}")