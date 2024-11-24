import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ComplexNumbersUI:
    def __init__(self, window, theme):
        self.window = window
        self.theme = theme
        self.window.title("Complex Numbers")
        self.window.geometry("800x600")
        
        # Create main container
        self.main_frame = ttk.Frame(window, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create input frame
        self.create_input_frame()
        
        # Create operation frame
        self.create_operation_frame()
        
        # Create visualization frame
        self.create_visualization_frame()
        
    def create_input_frame(self):
        input_frame = ttk.LabelFrame(self.main_frame, text="Complex Number Input", padding=10)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # First complex number
        ttk.Label(input_frame, text="First Complex Number (a + bi):").pack()
        number1_frame = ttk.Frame(input_frame)
        number1_frame.pack(fill=tk.X, pady=5)
        
        self.real1 = ttk.Entry(number1_frame, width=10)
        self.real1.pack(side=tk.LEFT, padx=5)
        ttk.Label(number1_frame, text="+").pack(side=tk.LEFT)
        self.imag1 = ttk.Entry(number1_frame, width=10)
        self.imag1.pack(side=tk.LEFT, padx=5)
        ttk.Label(number1_frame, text="i").pack(side=tk.LEFT)
        
        # Second complex number
        ttk.Label(input_frame, text="Second Complex Number (a + bi):").pack()
        number2_frame = ttk.Frame(input_frame)
        number2_frame.pack(fill=tk.X, pady=5)
        
        self.real2 = ttk.Entry(number2_frame, width=10)
        self.real2.pack(side=tk.LEFT, padx=5)
        ttk.Label(number2_frame, text="+").pack(side=tk.LEFT)
        self.imag2 = ttk.Entry(number2_frame, width=10)
        self.imag2.pack(side=tk.LEFT, padx=5)
        ttk.Label(number2_frame, text="i").pack(side=tk.LEFT)
    
    def create_operation_frame(self):
        op_frame = ttk.LabelFrame(self.main_frame, text="Operations", padding=10)
        op_frame.pack(fill=tk.X, padx=5, pady=5)
        
        button_frame = ttk.Frame(op_frame)
        button_frame.pack(fill=tk.X)
        
        operations = [
            ("Add", self.add_complex),
            ("Subtract", self.subtract_complex),
            ("Multiply", self.multiply_complex),
            ("Divide", self.divide_complex),
            ("Magnitude", self.calculate_magnitude),
            ("Phase", self.calculate_phase)
        ]
        
        for text, command in operations:
            ttk.Button(button_frame, text=text, command=command).pack(side=tk.LEFT, padx=5)
        
        # Result display
        self.result_label = ttk.Label(op_frame, text="Result: ", padding=10)
        self.result_label.pack(fill=tk.X)
    
    def create_visualization_frame(self):
        viz_frame = ttk.LabelFrame(self.main_frame, text="Visualization", padding=10)
        viz_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.ax.grid(True)
        self.ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        self.ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        self.ax.set_aspect('equal')
    
    def get_complex_numbers(self):
        try:
            z1 = complex(float(self.real1.get()), float(self.imag1.get()))
            z2 = complex(float(self.real2.get()), float(self.imag2.get()))
            return z1, z2
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
            return None, None
    
    def plot_complex_numbers(self, z1, z2, result=None):
        self.ax.clear()
        self.ax.grid(True)
        self.ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        self.ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Plot first number
        self.ax.plot([0, z1.real], [0, z1.imag], 'b-', label='z1')
        self.ax.plot(z1.real, z1.imag, 'bo')
        
        # Plot second number
        self.ax.plot([0, z2.real], [0, z2.imag], 'r-', label='z2')
        self.ax.plot(z2.real, z2.imag, 'ro')
        
        # Plot result if available
        if result is not None:
            self.ax.plot([0, result.real], [0, result.imag], 'g-', label='result')
            self.ax.plot(result.real, result.imag, 'go')
        
        self.ax.legend()
        self.ax.set_aspect('equal')
        self.canvas.draw()
    
    def add_complex(self):
        z1, z2 = self.get_complex_numbers()
        if z1 is not None and z2 is not None:
            result = z1 + z2
            self.result_label.config(text=f"Result: {result:.2f}")
            self.plot_complex_numbers(z1, z2, result)
    
    def subtract_complex(self):
        z1, z2 = self.get_complex_numbers()
        if z1 is not None and z2 is not None:
            result = z1 - z2
            self.result_label.config(text=f"Result: {result:.2f}")
            self.plot_complex_numbers(z1, z2, result)
    
    def multiply_complex(self):
        z1, z2 = self.get_complex_numbers()
        if z1 is not None and z2 is not None:
            result = z1 * z2
            self.result_label.config(text=f"Result: {result:.2f}")
            self.plot_complex_numbers(z1, z2, result)
    
    def divide_complex(self):
        z1, z2 = self.get_complex_numbers()
        if z1 is not None and z2 is not None:
            try:
                result = z1 / z2
                self.result_label.config(text=f"Result: {result:.2f}")
                self.plot_complex_numbers(z1, z2, result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero!")
    
    def calculate_magnitude(self):
        z1, _ = self.get_complex_numbers()
        if z1 is not None:
            magnitude = abs(z1)
            self.result_label.config(text=f"Magnitude: {magnitude:.2f}")
    
    def calculate_phase(self):
        z1, _ = self.get_complex_numbers()
        if z1 is not None:
            phase = np.angle(z1, deg=True)
            self.result_label.config(text=f"Phase: {phase:.2f}°")