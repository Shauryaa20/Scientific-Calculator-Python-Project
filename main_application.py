import tkinter as tk
from matrix_calculator_gui import MatrixCalculator
from equation_page import EquationPage 
from equation_solver import solve_linear, solve_quadratic, solve_cubic


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Choose an Operation", font=("Arial", 20)).pack(pady=20)

        tk.Button(self, text="Equation", font=("Arial", 14), width=20,
                  command=lambda: controller.show_frame("EquationPage")).pack(pady=10)
        tk.Button(self, text="Matrix", font=("Arial", 14), width=20,
                  command=lambda: controller.show_frame("MatrixPage")).pack(pady=10)
        tk.Button(self, text="Statistics", font=("Arial", 14), width=20).pack(pady=10)

class MatrixPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0) 
        self.rowconfigure(1, weight=1) 

        
        back_button = tk.Button(self, text="Back to Start", font=("Arial", 12),
                                command=lambda: controller.show_frame("StartPage"))
        back_button.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        calculator_frame = tk.Frame(self)
        calculator_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        MatrixCalculator(calculator_frame)

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Math Toolkit")
        self.geometry("800x600")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for Page in (StartPage, MatrixPage, EquationPage): 
            page_name = Page.__name__
            frame = Page(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

