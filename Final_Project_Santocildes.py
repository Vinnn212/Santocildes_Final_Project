import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Basic Calculator")

        # Entry widgets for user input
        self.number1 = tk.Entry(master, width=10)
        self.number1.grid(row=0, column=0, padx=5, pady=5)

        self.number2 = tk.Entry(master, width=10)
        self.number2.grid(row=0, column=1, padx=5, pady=5)

        # Dropdown menu for operation selection
        self.operations = ["Addition", "Subtraction", "Multiplication", "Division"]
        self.operation_var = tk.StringVar(master)
        self.operation_var.set(self.operations[0])  # default value

        self.operation_menu = tk.OptionMenu(master, self.operation_var, *self.operations)
        self.operation_menu.grid(row=0, column=2, padx=5, pady=5)

        # Button to perform the calculation
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=1, column=0, columnspan=3, pady=10)

        # Label to display the result
        self.result_label = tk.Label(master, text="Result: ")
        self.result_label.grid(row=2, column=0, columnspan=3)

    def calculate(self):
        try:
            num1 = float(self.number1.get())
            num2 = float(self.number2.get())
            operation = self.operation_var.get()

            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Cannot divide by zero"
            else:
                result = "Invalid operation"

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()

# Instantiate the CalculatorApp class
calculator_app = CalculatorApp(window)

# Run the application
window.mainloop()