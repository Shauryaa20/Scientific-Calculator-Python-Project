import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy import stats

class StatisticsUI:
    def __init__(self, window, theme):
        self.window = window
        self.theme = theme
        self.window.title("Statistical Analysis")
        self.window.geometry("1000x800")
        
        # Create main container
        self.main_frame = ttk.Frame(window, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create input frame
        self.create_input_frame()
        
        # Create analysis frame
        self.create_analysis_frame()
        
        # Create visualization frame
        self.create_visualization_frame()
    
    def create_input_frame(self):
        input_frame = ttk.LabelFrame(self.main_frame, text="Data Input", padding=10)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Enter numbers separated by commas:").pack()
        
        self.data_entry = tk.Text(input_frame, height=4, width=50)
        self.data_entry.pack(fill=tk.X, pady=5)
        
        button_frame = ttk.Frame(input_frame)
        button_frame.pack(fill=tk.X)
        
        ttk.Button(button_frame, text="Analyze", command=self.analyze_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Sample Data", command=self.load_sample_data).pack(side=tk.LEFT, padx=5)
    
    def create_analysis_frame(self):
        self.analysis_frame = ttk.LabelFrame(self.main_frame, text="Statistical Analysis", padding=10)
        self.analysis_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Create result labels
        self.results = {}
        for stat in ['Mean', 'Median', 'Mode', 'Std Dev', 'Variance', 'Range', 'Min', 'Max', 'Count']:
            frame = ttk.Frame(self.analysis_frame)
            frame.pack(fill=tk.X)
            ttk.Label(frame, text=f"{stat}:").pack(side=tk.LEFT)
            self.results[stat] = ttk.Label(frame, text="")
            self.results[stat].pack(side=tk.LEFT, padx=5)
    
    def create_visualization_frame(self):
        viz_frame = ttk.LabelFrame(self.main_frame, text="Visualizations", padding=10)
        viz_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create notebook for different plots
        self.notebook = ttk.Notebook(viz_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create figures for different plots
        self.histogram_fig, self.histogram_ax = plt.subplots(figsize=(6, 4))
        self.boxplot_fig, self.boxplot_ax = plt.subplots(figsize=(6, 4))
        
        # Create canvas for plots
        self.histogram_canvas = FigureCanvasTkAgg(self.histogram_fig, master=self.notebook)
        self.boxplot_canvas = FigureCanvasTkAgg(self.boxplot_fig, master=self.notebook)
        
        # Add plots to notebook
        self.notebook.add(self.histogram_canvas.get_tk_widget(), text="Histogram")
        self.notebook.add(self.boxplot_canvas.get_tk_widget(), text="Box Plot")
    
    def get_data(self):
        try:
            data_str = self.data_entry.get("1.0", tk.END).strip()
            data = [float(x.strip()) for x in data_str.split(',') if x.strip()]
            return np.array(data)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers separated by commas")
            return None
    
    def analyze_data(self):
        data = self.get_data()
        if data is None or len(data) == 0:
            return
        
        # Calculate statistics
        self.results['Mean'].config(text=f"{np.mean(data):.2f}")
        self.results['Median'].config(text=f"{np.median(data):.2f}")
        self.results['Mode'].config(text=f"{stats.mode(data)[0]:.2f}")
        self.results['Std Dev'].config(text=f"{np.std(data):.2f}")
        self.results['Variance'].config(text=f"{np.var(data):.2f}")
        self.results['Range'].config(text=f"{np.max(data) - np.min(data):.2f}")
        self.results['Min'].config(text=f"{np.min(data):.2f}")
        self.results['Max'].config(text=f"{np.max(data):.2f}")
        self.results['Count'].config(text=f"{len(data)}")
        
        # Update visualizations
        self.plot_histogram()