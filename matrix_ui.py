import tkinter as tk
from tkinter import ttk,messagebox
import numpy as np

class MatrixUI:
    def __init__(self,window:tk.Tk):
        self.window = window
        self.window.title("Matrix Operations")
        self.window.geometry('1000x600')
        
        self.main_container = ttk.Frame(window,padding=10)
        self.main_container.pack(fill=tk.BOTH,expand=True)
        
        self.create_input_panel()
        self.create_operations_panel()
        
    def create_input_panel(self):
        input_frame = ttk.LabelFrame(self.main_container,text="Matrix Input",padding=10)
        input_frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=(0,10))
        
        # Matrix a frame
        matrix_a_frame = ttk.LabelFrame(input_frame,text="Matrix A",padding=10)
        matrix_a_frame.pack(fill=tk.BOTH,expand=True,pady=(0,10))
        
        dimframe = ttk.Frame(matrix_a_frame,padding=10)
        dimframe.pack(fill=tk.X,pady=(0,10))
        
        ttk.Label(dimframe,text="Rows:").pack(side=tk.LEFT)
        self.rows_a = ttk.Spinbox(dimframe,from_=1,to=5,width=5)
        self.rows_a.pack(side=tk.LEFT,padx=5)
        ttk.Label(dimframe,text="Cols:").pack(side=tk.LEFT)
        self.cols_a = ttk.Spinbox(dimframe,from_=1,to=5,width=5)
        self.cols_a.pack(side=tk.LEFT,padx=5)
        ttk.Button(dimframe,text="Create Matrix A",command=lambda:self.create_matrix_input('A') ).pack(side=tk.LEFT,padx=5)
        
        self.a_frame = ttk.Frame(matrix_a_frame)
        self.a_frame.pack(fill=tk.BOTH,expand=True,pady=5)
        
        # Matrix b frame
        matrix_b_frame = ttk.LabelFrame(input_frame,text="Matrix B",padding=10)
        matrix_b_frame.pack(fill=tk.BOTH,expand=True,pady=(0,10))
        
        dimframe = ttk.Frame(matrix_b_frame,padding=10)
        dimframe.pack(fill=tk.X,pady=(0,10))
        
        ttk.Label(dimframe,text="Rows:").pack(side=tk.LEFT)
        self.rows_b = ttk.Spinbox(dimframe,from_=1,to=5,width=5)
        self.rows_b.pack(side=tk.LEFT,padx=5)
        ttk.Label(dimframe,text="Cols:").pack(side=tk.LEFT)
        self.cols_b = ttk.Spinbox(dimframe,from_=1,to=5,width=5)
        self.cols_b.pack(side=tk.LEFT,padx=5)
        ttk.Button(dimframe,text="Create Matrix B",command=lambda:self.create_matrix_input('B')).pack(side=tk.LEFT,padx=5)
        
        self.b_frame = ttk.Frame(matrix_b_frame)
        self.b_frame.pack(fill=tk.BOTH,expand=True,pady=5)
        
    def create_operations_panel(self):
        operations_panel = ttk.LabelFrame(self.main_container,text="Operations",padding=10)
        operations_panel.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)
        
        operations = [
            ("Addition (A + B)", self.add_matrices),
            ("Subtraction (A - B)", self.subtract_matrices),
            ("Dot Product (A.B)", self.dot_product_matrices),
            ("Multiplication (A × B)", self.multiply_matrices),
            ("Determinant", self.calculate_determinant),
            ("Inverse", self.calculate_inverse),
            ("Transpose", self.calculate_transpose)
        ]
        
        for text,cmd in operations:
            ttk.Button(operations_panel,text=text,command=cmd).pack(fill=tk.X,pady=5)
            
        result_frame = ttk.LabelFrame(operations_panel,text="Results",padding=10)
        result_frame.pack(fill=tk.BOTH,expand=True,pady=5)
        
        self.result_text = tk.Text(result_frame,height=10,wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH,expand=True)
        self.result_text.bind('<Key>',lambda x:'break')
    
    def create_matrix_input(self,label):
        frame = self.a_frame if label=='A' else self.b_frame
        rows = int(self.rows_a.get() if label=='A' else self.rows_b.get())
        cols = int(self.cols_a.get() if label=='A' else self.cols_b.get())
        
        for wid in frame.winfo_children():
            wid.destroy()
        
        entries = []
        for row in range(rows):
            row_entries = []
            for col in range(cols):
                entry = ttk.Entry(frame,width=8)
                entry.grid(row=row,column=col,padx=2,pady=2)
                row_entries.append(entry)
            entries.append(row_entries)
        
        if label == 'A':
            self.a_entries = entries
        else:
            self.b_entries = entries
    
    def get_matrix_from_entries(self,entries):
        rows = len(entries)
        cols = len(entries[0])
        matrix = np.zeros((rows,cols))
        for i in range(rows):
            for j in range(cols):
                matrix[i,j] = float(entries[i][j].get())
        return matrix
    
    def add_matrices(self):
        try:
            a = self.get_matrix_from_entries(self.a_entries)
            b = self.get_matrix_from_entries(self.b_entries)
            result = a + b
            self.display_results("Addition Result: ",result)
        except Exception as e:
            messagebox.showerror("Error","Invalid Operation")
    
    def subtract_matrices(self):
        try:
            a = self.get_matrix_from_entries(self.a_entries)
            b = self.get_matrix_from_entries(self.b_entries)
            result = a - b
            self.display_results("Subtraction Result: ",result)
        except Exception as e:
            messagebox.showerror("Error","Invalid Operation")
            
    def dot_product_matrices(self):
        try:
            a = self.get_matrix_from_entries(self.a_entries)
            b = self.get_matrix_from_entries(self.b_entries)
            result = a * b
            self.display_results("Dot Product of matricues: ",result)
        except Exception as e:
            messagebox.showerror("Error","Invalid Operation")
    
    def multiply_matrices(self):
        try:
            a = self.get_matrix_from_entries(self.a_entries)
            b = self.get_matrix_from_entries(self.b_entries)
            result = a @ b
            self.display_results("Multiplication Result: ",result)
        except Exception as e:
            messagebox.showerror("Error","Invalid Operation")
    
    def calculate_determinant(self):
        try:
            a = self.get_matrix_from_entries(self.a_entries)
            result = np.linalg.det(a)
            self.result_text.delete(1.0,tk.END)
            self.result_text.insert(tk.END,f"Determinant of Matrix A:  {result:8.4f}")
        except Exception as e:
            messagebox.showerror("Error","Invalid Operation")
    
    def calculate_inverse(self):
        try:
            a = self.get_matrix_from_entries(self.a_entries)
            result = np.linalg.inv(a)
            self.display_results("Inverse of Matrix A:",result)
        except Exception as e:
            messagebox.showerror("Error","Invalid Operation")
    
    def calculate_transpose(self):
        try:
            a = self.get_matrix_from_entries(self.a_entries)
            result = np.transpose(a)
            self.display_results("Transpose of Matrix A:",result)
        except Exception as e:
            messagebox.showerror("Error","Invalid Operation")
            
    def display_results(self,title,matrix):
        self.result_text.delete(1.0,tk.END)
        self.result_text.insert(tk.END,f"{title}\n\n")
        for row in matrix:
            row_text = " ".join(f"{col:8.4f}" for col in row)
            self.result_text.insert(tk.END,f"{row_text}\n")