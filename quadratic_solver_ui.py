import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class QuadraticSolverUI:
    def __init__(self, window, theme):
        self.window = window
        self.theme = theme
        self.window.title("Quadratic Equation Solver")
        self.window.geometry("800x600")

        # Create main container
        self.main_frame = ttk.Frame(window, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create input frame
        self.create_input_frame()

        # Create result frame
        self.create_result_frame()

        # Create plot frame
        self.create_plot_frame()

    def create_input_frame(self):
        input_frame = ttk.LabelFrame(self.main_frame, text="Enter Coefficients", padding=10)
        input_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Label(input_frame, text="ax² + bx + c = 0").pack()

        # Coefficient inputs
        coeff_frame = ttk.Frame(input_frame)
        coeff_frame.pack(fill=tk.X, pady=10)

        # a coefficient
        ttk.Label(coeff_frame, text="a = ").pack(side=tk.LEFT)
        self.a_entry = ttk.Entry(coeff_frame, width=8)
        self.a_entry.pack(side=tk.LEFT, padx=(0, 20))
        self.a_entry.insert(0, "1")

        # b coefficient
        ttk.Label(coeff_frame, text="b = ").pack(side=tk.LEFT)
        self.b_entry = ttk.Entry(coeff_frame, width=8)
        self.b_entry.pack(side=tk.LEFT, padx=(0, 20))
        self.b_entry.insert(0, "0")

        # c coefficient
        ttk.Label(coeff_frame, text="c = ").pack(side=tk.LEFT)
        self.c_entry = ttk.Entry(coeff_frame, width=8)
        self.c_entry.pack(side=tk.LEFT)
        self.c_entry.insert(0, "0")

        # Buttons
        button_frame = ttk.Frame(input_frame)
        button_frame.pack(fill=tk.X, pady=10)

        ttk.Button(button_frame, text="Solve", command=self.solve).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=5)

    def create_result_frame(self):
        self.result_frame = ttk.LabelFrame(self.main_frame, text="Results", padding=10)
        self.result_frame.pack(fill=tk.X, padx=5, pady=5)

        self.result_label = ttk.Label(self.result_frame, text="")
        self.result_label.pack()

    def create_plot_frame(self):
        plot_frame = ttk.LabelFrame(self.main_frame, text="Graph", padding=10)
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create figure and canvas
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def solve(self):
        try:
            # Get coefficients
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

            if a == 0:
                raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation")

            # Calculate discriminant
            discriminant = b**2 - 4*a*c

            # Calculate roots
            if discriminant > 0:
                x1 = (-b + np.sqrt(discriminant)) / (2*a)
                x2 = (-b - np.sqrt(discriminant)) / (2*a)
                result = f"Two real roots:\nx₁ = {x1:.4f}\nx₂ = {x2:.4f}"
            elif discriminant == 0:
                x = -b / (2*a)
                result = f"One real root:\nx = {x:.4f}"
            else:
                real = -b / (2*a)
                imag = np.sqrt(abs(discriminant)) / (2*a)
                result = f"Two complex roots:\nx₁ = {real:.4f} + {imag:.4f}i\nx₂ = {real:.4f} - {imag:.4f}i"

            self.result_label.config(text=result)
            self.plot_quadratic(a, b, c)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def plot_quadratic(self, a, b, c):
        self.ax.clear()
        
        # Generate x values
        x = np.linspace(-10, 10, 200)
        y = a*x**2 + b*x + c

        # Plot function
        self.ax.plot(x, y)
        self.ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        self.ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        self.ax.grid(True, alpha=0.3)
        
        # Set labels
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title(f'y = {a:g}x² + {b:g}x + {c:g}')

        # Update canvas
        self.canvas.draw()

    def clear(self):
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.c_entry.delete(0, tk.END)
        self.a_entry.insert(0, "1")
        self.b_entry.insert(0, "0")
        self.c_entry.insert(0, "0")
        self.result_label.config(text="")
        self.ax.clear()
        self.canvas.draw()