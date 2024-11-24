import tkinter as tk
from equation_solver import solve_linear, solve_quadratic, solve_cubic

class EquationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Title
        tk.Label(self, text="Choose an Equation", font=("Arial", 20)).pack(pady=10)

        # Equation options
        tk.Button(self, text="System of Linear Equations (ax + by = c)", font=("Arial", 14), width=30,
                  command=self.show_linear_solver).pack(pady=5)
        tk.Button(self, text="Quadratic Equation (ax² + bx + c = 0)", font=("Arial", 14), width=30,
                  command=self.show_quadratic_solver).pack(pady=5)
        tk.Button(self, text="Cubic Equation (ax³ + bx²+ cx + d = 0)", font=("Arial", 14), width=30,
                  command=self.show_cubic_solver).pack(pady=5)

        # Back Button
        tk.Button(self, text="Back to Start", font=("Arial", 12),
                  command=lambda: controller.show_frame("StartPage")).pack(pady=20)

    def show_linear_solver(self):
        self.display_linear_input_fields()

    def show_quadratic_solver(self):
        self.display_input_fields(["a", "b", "c"], solve_quadratic)

    def show_cubic_solver(self):
        self.display_input_fields(["a", "b", "c", "d"], solve_cubic)

    def display_linear_input_fields(self):
        self.clear_page()

        tk.Label(self, text="Enter Coefficients for Two Equations", font=("Arial", 16)).pack(pady=10)

        entries = {
            "Equation 1": {"a": None, "b": None, "c": None},
            "Equation 2": {"a": None, "b": None, "c": None},
        }

        for eq_label, coeffs in entries.items():
            frame = tk.Frame(self)
            frame.pack(pady=5)
            tk.Label(frame, text=eq_label, font=("Arial", 12, "bold")).pack(side="top")

            for label in ["a", "b", "c"]:
                sub_frame = tk.Frame(frame)
                sub_frame.pack(pady=2)
                tk.Label(sub_frame, text=f"{label}:", font=("Arial", 12)).pack(side="left", padx=5)
                entry = tk.Entry(sub_frame, font=("Arial", 12), width=10)
                entry.pack(side="left", padx=5)
                coeffs[label] = entry

        result_label = tk.Label(self, text="", font=("Arial", 12), fg="blue")
        result_label.pack(pady=10)

        def calculate_result():
            try:
                coefficients1 = {key: float(entries["Equation 1"][key].get()) for key in ["a", "b", "c"]}
                coefficients2 = {key: float(entries["Equation 2"][key].get()) for key in ["a", "b", "c"]}
                result = solve_linear(coefficients1, coefficients2)
                result_label.config(text=f"Result: x = {result[0]}, y = {result[1]}")
            except ValueError:
                result_label.config(text="Error: Enter valid numbers!")
            except Exception as e:
                result_label.config(text=f"Error: {e}")

        tk.Button(self, text="Calculate", font=("Arial", 12), command=calculate_result).pack(pady=10)

    def display_input_fields(self, labels, solve_function):
        self.clear_page()

        tk.Label(self, text="Enter Coefficients", font=("Arial", 16)).pack(pady=10)
        entries = {}

        for label in labels:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            tk.Label(frame, text=f"{label}:", font=("Arial", 12)).pack(side="left", padx=5)
            entry = tk.Entry(frame, font=("Arial", 12), width=10)
            entry.pack(side="left", padx=5)
            entries[label] = entry

        result_label = tk.Label(self, text="", font=("Arial", 12), fg="blue")
        result_label.pack(pady=10)

        def calculate_result():
            try:
                coefficients = {label: float(entries[label].get()) for label in labels}
                result = solve_function(**coefficients)
                result_label.config(text=f"Result: {result}")
            except ValueError:
                result_label.config(text="Error: Enter valid numbers!")

        tk.Button(self, text="Calculate", font=("Arial", 12), command=calculate_result).pack(pady=10)

    def clear_page(self):
        for widget in self.winfo_children():
            widget.destroy()
