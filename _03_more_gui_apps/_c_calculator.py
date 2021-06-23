"""
Create a simple calculator app
"""
import tkinter as tk

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # text fields
        self.field1 = tk.Entry(self)
        self.field1.place(relx=0.1, rely=0.1, relwidth=0.35, height=30)

        self.field2 = tk.Entry(self)
        self.field2.place(relx=0.55, rely=0.1, relwidth=0.35, height=30)

        # buttons
        self.addbutton = tk.Button(self, text='Add (+)', fg='black',
                                font=('courier new', 16, 'bold'), command=self.add)
        self.addbutton.place(relx=0.05, rely=0.4, relwidth=0.15, relheight=0.2)

        self.subtractbutton = tk.Button(self, text='Subtract (-)', fg='black',
                                font=('courier new', 16, 'bold'), command=self.subtract)
        self.subtractbutton.place(relx=0.3, rely=0.4, relwidth=0.15, relheight=0.2)

        self.multiplybutton = tk.Button(self, text='Multiply (x)', fg='black',
                                font=('courier new', 16, 'bold'), command=self.multiply)
        self.multiplybutton.place(relx=0.55, rely=0.4, relwidth=0.15, relheight=0.2)

        self.dividebutton = tk.Button(self, text='Divide (/)', fg='black',
                                font=('courier new', 16, 'bold'), command=self.divide)
        self.dividebutton.place(relx=0.8, rely=0.4, relwidth=0.15, relheight=0.2)

        # answer label
        self.answerfield = tk.Label(self, bg='white', font=('Rockwell', 20, 'normal', 'underline'))
        self.answerfield.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)

    def add(self):
        num1 = int(self.field1.get())
        num2 = int(self.field2.get())
        sum = num1 + num2
        print(sum)
        self.answerfield.configure(text=str(sum))

    def subtract(self):
        num1 = int(self.field1.get())
        num2 = int(self.field2.get())
        difference = num1 - num2
        self.answerfield.configure(text=str(difference))

    def multiply(self):
        num1 = int(self.field1.get())
        num2 = int(self.field2.get())
        product = num1 * num2
        self.answerfield.configure(text=str(product))

    def divide(self):
        num1 = int(self.field1.get())
        num2 = int(self.field2.get())
        quotient = num1 / num2
        self.answerfield.configure(text=str(quotient))

if __name__ == '__main__':
    app = Calculator()
    app.title('Calculator')
    app.geometry('800x200')
    app.mainloop()
