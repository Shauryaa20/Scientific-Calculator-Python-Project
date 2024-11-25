import tkinter as tk
from tkinter import ttk
import matrix_ui
import graphing_ui

class MathTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Tools")
        self.root.geometry("600x400")
        
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.configure_styles()
        ttk.Label(self.main_frame, text="Math Tools", style='Header.TLabel').pack(anchor='w', pady=(0, 20))
        self.create_tools_section()
    
    def configure_styles(self):
        style = ttk.Style()
        style.configure('Header.TLabel',font=('Segoe UI', 24, 'bold'),foreground='#1a73e8')
        style.configure('Tool.TFrame',background='#ffffff',relief='solid')
        style.configure('ToolTitle.TLabel',font=('Segoe UI', 14, 'bold'),foreground='#202124')
        style.configure('ToolDesc.TLabel',font=('Segoe UI', 10),foreground='#5f6368')
        style.configure('Open.TButton',font=('Segoe UI', 10),padding=5)
        
    def create_tools_section(self):
        tools_frame = ttk.Frame(self.main_frame)
        tools_frame.pack(fill=tk.BOTH, expand=True)
        
        tools = [
            ('Graphing Tool','Plot and analyze mathematical functions',self.open_graphing),
            ('Matrix Operations','Perform various matrix operations',self.open_matrix)
        ]
        
        for title,desc,cmd in tools:
            section = ttk.Frame(tools_frame, style='Tool.TFrame', padding=10)
            section.pack(fill=tk.X, pady=5)
            
            info_frame = ttk.Frame(section)
            info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            ttk.Label(info_frame,text=title,style='ToolTitle.TLabel').pack(anchor='w')
            ttk.Label(info_frame,text=desc,style='ToolDesc.TLabel').pack(anchor='w', pady=(2, 0))
            ttk.Button(section,text="Open →",style='Open.TButton',command=cmd).pack(side=tk.RIGHT)
    
    def open_matrix(self):
        window = tk.Toplevel(self.root)
        matrix_ui.MatrixUI(window)
    
    def open_graphing(self):
        window = tk.Toplevel(self.root)
        graphing_ui.GraphingUI(window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathTool(root)
    root.mainloop()