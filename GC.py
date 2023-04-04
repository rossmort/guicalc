import tkinter as tk

class GraphicalCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphical Calculator")
        self.result = tk.StringVar()
        self.result.set("0")
        self.equation = ""

        # Create result display
        self.result_display = tk.Label(master, textvariable=self.result, font=("Arial", 16), width=20, height=2, anchor="e")
        self.result_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, font=("Arial", 16), width=5, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, text):
        if text == "=":
            self.result.set(str(eval(self.equation)))
            self.equation = ""
        elif text == "C":
            self.result.set("0")
            self.equation = ""
        else:
            if self.result.get() == "0":
                self.result.set("")
            self.equation += text
            self.result.set(self.equation)

root = tk.Tk()
calculator = GraphicalCalculator(root)
root.mainloop()
