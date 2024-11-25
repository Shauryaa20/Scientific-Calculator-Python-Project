import tkinter as tk
from tkinter import ttk,messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class GraphingUI:
    def __init__(self,window:tk.Tk):
        self.window = window
        self.window.title('Graph Plotter')
        self.window.geometry('1000x600')
        
        self.main_container = ttk.Frame(window,padding=10)
        self.main_container.pack(fill=tk.BOTH,expand=True)
        
        self.create_input_panel()
        self.create_graph_panel()
        self.initialize_plot()
    
    def create_input_panel(self):
        self.input_frame = ttk.LabelFrame(self.main_container,text="Graph Settings",padding=10)
        self.input_frame.pack(side=tk.LEFT,fill=tk.Y,padx=(0,10))
        
        ttk.Label(self.input_frame,text="Function:").pack(anchor=tk.W,pady=(0,5))
        self.function_var = tk.StringVar(value="x^2")
        self.function_entry = tk.Entry(self.input_frame,textvariable=self.function_var,width=30)
        self.function_entry.pack(fill=tk.X,pady=(0,10))
        
        # Range Frame
        range_frame = ttk.Frame(self.input_frame,padding=10)
        range_frame.pack(fill=tk.X,pady=(0,10))
        
        ttk.Label(range_frame,text="X-range: ").grid(row=0,column=0)
        self.min_x = ttk.Entry(range_frame,width=8)
        self.min_x.insert(0,'-10')
        self.min_x.grid(row=0,column=1,padx=5)
        ttk.Label(range_frame,text=" to ").grid(row=0,column=2)
        self.max_x = ttk.Entry(range_frame,width=8)
        self.max_x.insert(0,'10')
        self.max_x.grid(row=0,column=3,padx=5)
        
        # Style frame
        style_frame = ttk.LabelFrame(self.input_frame,text='Plot Style',padding=10)
        style_frame.pack(fill=tk.X,pady=(0,10))
        
        ttk.Label(style_frame,text="Color:").pack(anchor=tk.W)
        self.color_var = tk.StringVar(value='blue')
        color_options = ['blue','red','green','yellow','orange','purple']
        color_menu = ttk.OptionMenu(style_frame,self.color_var,color_options[0],*color_options,command=lambda _:self.update_plot())
        color_menu.pack(fill=tk.X,padx=5)
        
        ttk.Label(style_frame,text="Line style:").pack(anchor=tk.W)
        self.line_style_var = tk.StringVar(value='-')
        line_style_options = ['-','--',':']
        line_style_menu = ttk.OptionMenu(style_frame,self.line_style_var,line_style_options[0],*line_style_options,command=lambda _:self.update_plot())
        line_style_menu.pack(fill=tk.X,padx=5)
        
        # Grid options
        grid_option_frame = ttk.LabelFrame(self.input_frame,text="Grid options",padding=10)
        grid_option_frame.pack(fill=tk.X,pady=(0,10))
        
        self.show_grid = tk.BooleanVar(value=1)
        ttk.Checkbutton(grid_option_frame,text="Show grid",variable=self.show_grid,command=self.update_plot).pack(anchor=tk.W)
        self.show_axes = tk.BooleanVar(value=1)
        ttk.Checkbutton(grid_option_frame,text="Show axes",variable=self.show_axes,command=self.update_plot).pack(anchor=tk.W)
        
        # Buttons
        button_frame = ttk.Frame(self.input_frame,padding=10)
        button_frame.pack(fill=tk.X,pady=(0,10))
        
        ttk.Button(button_frame,text="Plot",command=self.update_plot).grid(row=0,column=0,padx=10)
        ttk.Button(button_frame,text="Clear",command=self.clear_plot).grid(row=0,column=1,padx=10)
        
    def create_graph_panel(self):
        self.graph_frame = ttk.LabelFrame(self.main_container,text="Graph",padding=10)
        self.graph_frame.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)
    
    def initialize_plot(self):
        self.fig = Figure(figsize=(10,6),dpi=100)
        self.ax = self.fig.add_subplot(1,1,1)
        
        self.canvas = FigureCanvasTkAgg(self.fig,master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)
        
        self.update_plot()
    
    def parse_function(self):
        funct_str = self.function_var.get().replace('^','**')
        safe_funcs = {
            'sin' : np.sin,
            'cos' : np.cos,
            'tan' : np.tan,
            'log' : np.log,
            'sqrt' : np.sqrt,
            'pi' : np.pi,
            'e' : np.e,
            'abs' : np.abs,
            'x' : None
        }
        try:
            def func(x):
                safe_funcs['x'] = x
                return eval(funct_str,{"__builtin__":None},safe_funcs)
            return func
        except:
            raise ValueError('Invalid Expression')
    
    def update_plot(self):
        try:
            self.ax.clear()
                
            x_min = float(self.min_x.get())
            x_max = float(self.max_x.get())
            
            x = np.linspace(x_min,x_max,1000)
            func = self.parse_function()
            y = func(x)
            
            self.ax.plot(x,y,color=self.color_var.get(),
                         linestyle = self.line_style_var.get(),
                         label=self.function_var.get())
            
            self.ax.grid(self.show_grid.get())
            if(self.show_axes.get()):
                self.ax.axhline(y=0,color='k',linestyle='-',alpha=0.4)
                self.ax.axvline(x=0,color='k',linestyle='-',alpha=0.4)
                
            self.ax.legend()
            self.canvas.draw()    
        except ValueError as e:
            messagebox.showerror('Error',str(e))
        except Exception as e:
            messagebox.showerror('Error',str(e))
    
    def clear_plot(self):
        self.ax.clear()
        self.ax.grid(self.show_grid.get())
        if(self.show_axes.get()):
            self.ax.axhline(y=0,color='k',linestyle='-',alpha=0.4)
            self.ax.axvline(x=0,color='k',linestyle='-',alpha=0.4)
        self.canvas.draw()