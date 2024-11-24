# main.py
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from PIL import Image, ImageTk
import linear_solver_ui
import quadratic_solver_ui
import statistics_ui
import matrix_ui
import graphing_ui
import complex_numbers_ui

class ThemeManager:
    LIGHT_THEME = {
        'bg': '#f0f0f0',
        'fg': '#333333',
        'button_bg': '#e0e0e0',
        'highlight': '#007acc',
        'tile_bg': '#ffffff'
    }
    
    DARK_THEME = {
        'bg': '#2d2d2d',
        'fg': '#ffffff',
        'button_bg': '#3d3d3d',
        'highlight': '#0098ff',
        'tile_bg': '#363636'
    }
    
    @classmethod
    def get_theme(cls, is_dark):
        return cls.DARK_THEME if is_dark else cls.LIGHT_THEME

class MathTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Math Tool")
        self.root.geometry("800x600")
        
        # Initialize theme
        self.is_dark_theme = False
        self.current_theme = ThemeManager.get_theme(self.is_dark_theme)
        
        # Create main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header
        self.create_header()
        
        # Create scrollable tile frame
        self.create_scrollable_tile_frame()
        
        # Create tiles
        self.create_tiles()
        
        # Create status bar
        self.create_status_bar()
        
        # Configure style
        self.configure_styles()
        
    def configure_styles(self):
        style = ttk.Style()
        style.configure('Tile.TButton', 
                       padding=20,
                       font=('Helvetica', 12),
                       width=20,
                       height=8)
        
        style.configure('Header.TLabel',
                       font=('Helvetica', 24, 'bold'),
                       padding=10)
                       
        style.configure('Status.TLabel',
                       font=('Helvetica', 10),
                       padding=5)
    
    def create_header(self):
        header_frame = ttk.Frame(self.main_container)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(header_frame, 
                               text="Advanced Math Tool",
                               style='Header.TLabel')
        title_label.pack(side=tk.LEFT)
        
        # Theme toggle button
        # self.theme_button = ttk.Button(header_frame,
        #                              text="🌙 Dark Mode" if not self.is_dark_theme else "☀️ Light Mode",
        #                              command=self.toggle_theme)
        # self.theme_button.pack(side=tk.RIGHT)
    
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
        
        # Configure tile frame grid
        self.tile_frame.grid_columnconfigure(0, weight=1)
        self.tile_frame.grid_columnconfigure(1, weight=1)
        self.tile_frame.grid_columnconfigure(2, weight=1)
        
        # Bind resize event
        self.tile_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
    def create_tiles(self):
        tiles_info = [
            ("Linear Equations", "Solve systems of linear equations", self.open_linear_solver),
            ("Quadratic Equations", "Solve quadratic equations with real or complex roots", self.open_quadratic_solver),
            ("Statistics", "Calculate statistical measures and visualizations", self.open_statistics),
            ("Matrix Operations", "Perform various matrix operations", self.open_matrix),
            ("Graphing", "Plot functions and data", self.open_graphing),
            ("Complex Numbers", "Work with complex numbers", self.open_complex)
        ]
        
        for idx, (title, desc, command) in enumerate(tiles_info):
            row = idx // 3
            col = idx % 3
            self.create_tile(title, desc, row, col, command)
    
    def create_tile(self, title, description, row, col, command):
        tile_frame = ttk.Frame(self.tile_frame, style='Tile.TFrame')
        tile_frame.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
        
        btn = ttk.Button(tile_frame, 
                        text=f"{title}\n\n{description}",
                        style='Tile.TButton',
                        command=command)
        btn.pack(expand=True, fill=tk.BOTH)
    
    def create_status_bar(self):
        self.status_bar = ttk.Label(self.root,
                                  text="Ready",
                                  style='Status.TLabel')
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def toggle_theme(self):
        self.is_dark_theme = not self.is_dark_theme
        self.current_theme = ThemeManager.get_theme(self.is_dark_theme)
        self.theme_button.configure(text="🌙 Dark Mode" if not self.is_dark_theme else "☀️ Light Mode")
        self.apply_theme()
    
    def apply_theme(self):
        style = ttk.Style()
        theme = self.current_theme
        
        # Configure styles with new theme colors
        style.configure('Tile.TFrame', background=theme['tile_bg'])
        style.configure('Tile.TButton', background=theme['button_bg'], foreground=theme['fg'])
        style.configure('Header.TLabel', background=theme['bg'], foreground=theme['fg'])
        style.configure('Status.TLabel', background=theme['bg'], foreground=theme['fg'])
        
        # Apply theme to main window
        self.root.configure(bg=theme['bg'])
        self.canvas.configure(bg=theme['bg'])
        self.tile_frame.configure(bg=theme['bg'])
    
    def update_status(self, message):
        self.status_bar.configure(text=message)
    
    def open_linear_solver(self):
        self.update_status("Opening Linear Equation Solver...")
        window = tk.Toplevel(self.root)
        linear_solver_ui.LinearSolverUI(window, self.current_theme)
        self.update_status("Ready")
    
    def open_quadratic_solver(self):
        self.update_status("Opening Quadratic Equation Solver...")
        window = tk.Toplevel(self.root)
        quadratic_solver_ui.QuadraticSolverUI(window, self.current_theme)
        self.update_status("Ready")
    
    def open_statistics(self):
        self.update_status("Opening Statistics Calculator...")
        window = tk.Toplevel(self.root)
        statistics_ui.StatisticsUI(window, self.current_theme)
        self.update_status("Ready")
    
    def open_matrix(self):
        self.update_status("Opening Matrix Operations...")
        window = tk.Toplevel(self.root)
        matrix_ui.MatrixUI(window, self.current_theme)
        self.update_status("Ready")
    
    def open_graphing(self):
        self.update_status("Opening Graphing Tool...")
        window = tk.Toplevel(self.root)
        graphing_ui.GraphingUI(window, self.current_theme)
        self.update_status("Ready")
    
    def open_complex(self):
        self.update_status("Opening Complex Number Calculator...")
        window = tk.Toplevel(self.root)
        complex_numbers_ui.ComplexNumbersUI(window, self.current_theme)
        self.update_status("Ready")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathTool(root)
    root.mainloop()