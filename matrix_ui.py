# matrix_ui.py
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from matrix_utils import *

class MatrixUI:
    def __init__(self, window, theme):
        self.window = window
        self.theme = theme
        self.window.title("Matrix Operations")
        self.window.geometry("1000x600")
        
        # Create main container
        self.main_container = ttk.Frame(window, padding=10)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create left panel for matrix input
        self.create_input_panel()
        
        # Create right panel for operations and results
        self.create_operation_panel()
        
        # Initialize matrices
        self.matrix_a = None
        self.matrix_b = None
    
    def create_input_panel(self):
        input_frame = ttk.LabelFrame(self.main_container, text="Matrix Input", padding=10)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Matrix A input
        matrix_a_frame = ttk.LabelFrame(input_frame, text="Matrix A", padding=10)
        matrix_a_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Matrix dimensions
        dim_frame = ttk.Frame(matrix_a_frame)
        dim_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(dim_frame, text="Rows:").pack(side=tk.LEFT)
        self.rows_a = ttk.Spinbox(dim_frame, from_=1, to=5, width=5)
        self.rows_a.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(dim_frame, text="Columns:").pack(side=tk.LEFT)
        self.cols_a = ttk.Spinbox(dim_frame, from_=1, to=5, width=5)
        self.cols_a.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(dim_frame, text="Create Matrix A", 
                  command=lambda: self.create_matrix_inputs('A')).pack(side=tk.LEFT, padx=5)
        
        # Frame for matrix A entries
        self.matrix_a_entries_frame = ttk.Frame(matrix_a_frame)
        self.matrix_a_entries_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Matrix B input (similar structure)
        matrix_b_frame = ttk.LabelFrame(input_frame, text="Matrix B", padding=10)
        matrix_b_frame.pack(fill=tk.BOTH, expand=True)
        
        dim_frame_b = ttk.Frame(matrix_b_frame)
        dim_frame_b.pack(fill=tk.X, pady=5)
        
        ttk.Label(dim_frame_b, text="Rows:").pack(side=tk.LEFT)
        self.rows_b = ttk.Spinbox(dim_frame_b, from_=1, to=5, width=5)
        self.rows_b.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(dim_frame_b, text="Columns:").pack(side=tk.LEFT)
        self.cols_b = ttk.Spinbox(dim_frame_b, from_=1, to=5, width=5)
        self.cols_b.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(dim_frame_b, text="Create Matrix B",
                  command=lambda: self.create_matrix_inputs('B')).pack(side=tk.LEFT, padx=5)
        
        self.matrix_b_entries_frame = ttk.Frame(matrix_b_frame)
        self.matrix_b_entries_frame.pack(fill=tk.BOTH, expand=True, pady=5)
    
    def create_operation_panel(self):
        operation_frame = ttk.LabelFrame(self.main_container, text="Operations", padding=10)
        operation_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Buttons for operations
        operations = [
            ("Addition (A + B)", self.add_matrices),
            ("Subtraction (A - B)", self.subtract_matrices),
            ("Multiplication (A × B)", self.multiply_matrices),
            ("Determinant", self.calculate_determinant),
            ("Inverse", self.calculate_inverse),
            ("Transpose", self.calculate_transpose)
        ]
        
        for text, command in operations:
            ttk.Button(operation_frame, text=text, command=command).pack(fill=tk.X, pady=2)
        
        # Result display
        result_frame = ttk.LabelFrame(operation_frame, text="Result", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.result_text = tk.Text(result_frame, height=10, wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, expand=True)
    
    def create_matrix_inputs(self, matrix_label):
        frame = self.matrix_a_entries_frame if matrix_label == 'A' else self.matrix_b_entries_frame
        rows = int(self.rows_a.get() if matrix_label == 'A' else self.rows_b.get())
        cols = int(self.cols_a.get() if matrix_label == 'A' else self.cols_b.get())
        
        # Clear existing entries
        for widget in frame.winfo_children():
            widget.destroy()
        
        # Create new entries
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = ttk.Entry(frame, width=8)
                entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            entries.append(row_entries)
        
        if matrix_label == 'A':
            self.matrix_a_entries = entries
        else:
            self.matrix_b_entries = entries
    
    def get_matrix_from_entries(self, entries):
        if not entries:
            return None
        
        rows = len(entries)
        cols = len(entries[0])
        matrix = np.zeros((rows, cols))
        
        for i in range(rows):
            for j in range(cols):
                try:
                    matrix[i, j] = float(entries[i][j].get())
                except ValueError:
                    messagebox.showerror("Error", f"Invalid value at position ({i+1}, {j+1})")
                    return None
        
        return matrix
    
    def add_matrices(self):
        try:
            a = self.get_matrix_from_entries(self.matrix_a_entries)
            b = self.get_matrix_from_entries(self.matrix_b_entries)
            
            if a is None or b is None:
                return
            
            result = matrix_add(a, b)
            self.display_result("Addition Result:", result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid operation")
    
    def subtract_matrices(self):
        try:
            a = self.get_matrix_from_entries(self.matrix_a_entries)
            b = self.get_matrix_from_entries(self.matrix_b_entries)
            
            if a is None or b is None:
                return
            
            result = matrix_subtract(a, b)
            self.display_result("Subtraction Result:", result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid operation")
    
    def multiply_matrices(self):
        try:
            a = self.get_matrix_from_entries(self.matrix_a_entries)
            b = self.get_matrix_from_entries(self.matrix_b_entries)
            
            if a is None or b is None:
                return
            
            result = matrix_multiply(a, b)
            self.display_result("Multiplication Result:", result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid operation")
    
    def calculate_determinant(self):
        try:
            matrix = self.get_matrix_from_entries(self.matrix_a_entries)
            if matrix is None:
                return
            
            result = matrix_determinant(matrix)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Determinant of Matrix A: {result:.4f}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid operation")
    
    def calculate_inverse(self):
        try:
            matrix = self.get_matrix_from_entries(self.matrix_a_entries)
            if matrix is None:
                return
            
            result = matrix_inverse(matrix)
            self.display_result("Inverse of Matrix A:", result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid operation")
    
    def calculate_transpose(self):
        try:
            matrix = self.get_matrix_from_entries(self.matrix_a_entries)
            if matrix is None:
                return
            
            result = matrix_transpose(matrix)
            self.display_result("Transpose of Matrix A:", result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid operation")
    
    def display_result(self, title, matrix):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"{title}\n\n")
        
        if isinstance(matrix, np.ndarray):
            rows, cols = matrix.shape
            for i in range(rows):
                row_text = " ".join(f"{matrix[i,j]:8.4f}" for j in range(cols))
                self.result_text.insert(tk.END, f"{row_text}\n")
        else:
            self.result_text.insert(tk.END, str(matrix))