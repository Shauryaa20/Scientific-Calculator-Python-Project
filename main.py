# main.py
import tkinter as tk
from tkinter import ttk
import linear_solver_ui
import quadratic_solver_ui
import matrix_ui
import graphing_ui
import complex_numbers_ui

class MathTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Math Tool")
        self.root.geometry("600x600")
        
        # Create main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header
        self.create_header()
        
        # Create scrollable tile frame
        self.create_scrollable_tile_frame()
        
        # Create tiles
        self.create_tiles()
        
        # Configure style
        self.configure_styles()
        
    def configure_styles(self):
        style = ttk.Style()
        style.configure('Tile.TButton', 
                       padding=20,
                       font=('Georgia', 12),
                       width=20,
                       height=15)
        
        style.configure('Header.TLabel',
                       font=('Helvetica', 24, 'bold'),
                       padding=10)
    
    def create_header(self):
        header_frame = ttk.Frame(self.main_container)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(header_frame, 
                               text="Advanced Math Tool",
                               style='Header.TLabel')
        title_label.pack(side=tk.LEFT)
    
    def create_scrollable_tile_frame(self):
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(self.main_container)
        scrollbar = ttk.Scrollbar(self.main_container, orient=tk.VERTICAL, command=self.canvas.yview)
        
        # Create frame for tiles
        self.tile_frame = ttk.Frame(self.canvas)
        
        # Configure canvas
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Add tile frame to canvas
        self.canvas.create_window((0, 0), window=self.tile_frame, anchor=tk.NW)
        
        # Configure tile frame grid - 2 columns
        self.tile_frame.grid_columnconfigure(0, weight=1)
        self.tile_frame.grid_columnconfigure(1, weight=1)
        
        # Bind resize event
        self.tile_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
    def create_tiles(self):
        tiles_info = [
            ("Linear Equations", "[Solve systems of linear \nequations]", self.open_linear_solver),
            ("Quadratic Equations", "[Solve quadratic equations \nwith real or complex roots]", self.open_quadratic_solver),
            ("Matrix Operations", "[Perform various matrix \noperations]", self.open_matrix),
            ("Graphing", "[Plot functions and data]", self.open_graphing),
            ("Complex Numbers", "[Work with complex \nnumbers]", self.open_complex)
        ]
        
        for idx, (title, desc, command) in enumerate(tiles_info):
            row = idx // 2
            col = idx % 2
            self.create_tile(title, desc, row, col, command)
    
    def create_tile(self, title, description, row, col, command):
        tile_frame = ttk.Frame(self.tile_frame, style='Tile.TFrame')
        tile_frame.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
        
        btn = ttk.Button(tile_frame, 
                        text=f"{title}\n\n{description}",
                        style='Tile.TButton',
                        command=command)
        btn.pack(expand=True, fill=tk.BOTH)
    
    def open_linear_solver(self):
        window = tk.Toplevel(self.root)
        linear_solver_ui.LinearSolverUI(window, None)
    
    def open_quadratic_solver(self):
        window = tk.Toplevel(self.root)
        quadratic_solver_ui.QuadraticSolverUI(window, None)
    
    def open_matrix(self):
        window = tk.Toplevel(self.root)
        matrix_ui.MatrixUI(window, None)
    
    def open_graphing(self):
        window = tk.Toplevel(self.root)
        graphing_ui.GraphingUI(window, None)
    
    def open_complex(self):
        window = tk.Toplevel(self.root)
        complex_numbers_ui.ComplexNumbersUI(window, None)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathTool(root)
    root.mainloop()