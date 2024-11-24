import tkinter as tk
from tkinter import messagebox
from matrix_operations import add_matrices, subtract_matrices, multiply_matrices

class MatrixCalculator:
    def __init__(self, parent):
        self.parent = parent  
        self.matrix_size = tk.IntVar(value=2)  
        self.setup_matrix_size_selector()

    def setup_matrix_size_selector(self):
        
        frame = tk.Frame(self.parent)
        frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        for i in range(2):
            frame.columnconfigure(i, weight=1)
        frame.rowconfigure(2, weight=1)

        tk.Label(frame, text="Select Matrix Size", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)
        tk.Radiobutton(frame, text="2x2", variable=self.matrix_size, value=2).grid(row=1, column=0, padx=10, sticky="ew")
        tk.Radiobutton(frame, text="3x3", variable=self.matrix_size, value=3).grid(row=1, column=1, padx=10, sticky="ew")
        tk.Button(frame, text="Next", command=self.get_matrix_input, width=10, height=2).grid(row=2, column=0, columnspan=2, pady=20)

    def get_matrix_input(self):

        for widget in self.parent.winfo_children():
            widget.destroy()

        size = self.matrix_size.get()
        self.matrix1_entries = []
        self.matrix2_entries = []

        frame = tk.Frame(self.parent)
        frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        for i in range(size + 5):  
            frame.rowconfigure(i, weight=1)
        for j in range(size * 2 + 3):  
            frame.columnconfigure(j, weight=1)

        # Input for Matrix 1
        tk.Label(frame, text="Enter Matrix 1 Elements", font=("Arial", 12)).grid(row=0, column=0, columnspan=size, pady=10)
        for i in range(size):
            row = []
            for j in range(size):
                entry = tk.Entry(frame, width=5, justify="center", font=("Arial", 12))  
                entry.grid(row=i + 1, column=j, padx=5, pady=5, sticky="ew")
                row.append(entry)
            self.matrix1_entries.append(row)

        tk.Label(frame, text="Enter Matrix 2 Elements", font=("Arial", 12)).grid(row=0, column=size + 1, columnspan=size, pady=10)
        for i in range(size):
            row = []
            for j in range(size):
                entry = tk.Entry(frame, width=5, justify="center", font=("Arial", 12))  
                entry.grid(row=i + 1, column=j + size + 1, padx=5, pady=5, sticky="ew")
                row.append(entry)
            self.matrix2_entries.append(row)

        button_frame = tk.Frame(frame)
        button_frame.grid(row=size + 2, column=0, columnspan=size * 2 + 1, pady=10)

        for i in range(3):
            button_frame.columnconfigure(i, weight=1)

        tk.Button(button_frame, text="Add", command=lambda: self.perform_operation("add"), width=10).grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(button_frame, text="Subtract", command=lambda: self.perform_operation("subtract"), width=10).grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        tk.Button(button_frame, text="Multiply", command=lambda: self.perform_operation("multiply"), width=10).grid(row=0, column=2, padx=10, pady=5, sticky="ew")

        # Result Display
        tk.Label(frame, text="Result", font=("Arial", 12)).grid(row=size + 3, column=0, columnspan=size, pady=10)
        self.result_text = tk.Text(frame, height=size, width=40, font=("Arial", 12))
        self.result_text.grid(row=size + 4, column=0, columnspan=size * 2, padx=5, pady=5)

    def perform_operation(self, operation):
        try:
            size = self.matrix_size.get()
            matrix1 = [[int(self.matrix1_entries[i][j].get()) for j in range(size)] for i in range(size)]
            matrix2 = [[int(self.matrix2_entries[i][j].get()) for j in range(size)] for i in range(size)]

            if operation == "add":
                result = add_matrices(matrix1, matrix2)
            elif operation == "subtract":
                result = subtract_matrices(matrix1, matrix2)
            elif operation == "multiply":
                result = multiply_matrices(matrix1, matrix2)

            self.result_text.delete(1.0, tk.END)
            for row in result:
                self.result_text.insert(tk.END, "\t".join(map(str, row)) + "\n")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for the matrices.")

