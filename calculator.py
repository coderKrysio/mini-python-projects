# create a gui application for calculator using tkinter
# the calculator should be able to perform basic arithmetic operations like addition, subtraction, multiplication and division
import tkinter as tk

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cute Calculator")
        self.root.configure(bg="#f7f7fa")
        self.expression = ""
        self.result = None
        self.create_widgets()

    def create_widgets(self):
        display_frame = tk.Frame(self.root, bg="#f7f7fa")
        display_frame.pack(pady=(18, 8))
        self.display_var = tk.StringVar()
        self.display = tk.Entry(display_frame, textvariable=self.display_var, font=("Segoe UI", 22, "bold"), fg="#22223b", bg="#f7f7fa", bd=0, justify="right", relief="flat", width=15)
        self.display.pack(ipady=10)
        self.display_var.set("0")

        btn_frame = tk.Frame(self.root, bg="#f7f7fa")
        btn_frame.pack(pady=8)
        btn_style = {"font": ("Segoe UI", 16, "bold"), "bg": "#eebbc3", "fg": "#22223b", "activebackground": "#c9ada7", "activeforeground": "#22223b", "width": 4, "height": 2, "bd": 0}

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]
        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                action = lambda x=char: self.on_button_click(x)
                tk.Button(btn_frame, text=char, command=action, **btn_style).grid(row=r, column=c, padx=6, pady=6)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display_var.set("0")
        elif char == "=":
            try:
                # Only allow safe characters
                safe_expr = self.expression.replace("/", "/").replace("*", "*").replace("-", "-").replace("+", "+")
                self.result = eval(safe_expr)
                self.display_var.set(str(self.result))
                self.expression = str(self.result)
            except ZeroDivisionError:
                self.display_var.set("Error: Div by 0")
                self.expression = ""
            except Exception:
                self.display_var.set("Error")
                self.expression = ""
        else:
            if self.display_var.get() == "0" or self.display_var.get().startswith("Error"):
                self.expression = ""
            # Prevent consecutive operators
            operators = "+-*/"
            if char in operators:
                if not self.expression or self.expression[-1] in operators:
                    # Replace last operator if present
                    if self.expression and self.expression[-1] in operators:
                        self.expression = self.expression[:-1]
                    else:
                        # Don't allow operator at start
                        return
            self.expression += char
            self.display_var.set(self.expression)
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()