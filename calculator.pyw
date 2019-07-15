import tkinter as tk
from stack import Stack
import operator

__version__ = "3.0"
ARITHMETIC_OPERATORS = {
        "+":operator.add, 
        "-":operator.sub,
        "*":operator.mul,
        "/":operator.truediv,
        "**":operator.pow,
        "//":operator.floordiv,
        "%":operator.mod,
        }

def linear_search(tosearch, target):
    for i in tosearch:
        if i == target:
            return True
    return False

def calculate_with_polish(numbers, operations):
    """Calculate math using the reverse polish notation"""
    numbers.reverse()
    numbers.extend(operations)
    sum_stack = Stack()

    for val in numbers:
        if val in ARITHMETIC_OPERATORS:
            if sum_stack.get_len() < 2:
                return
            val_1 = sum_stack.pop()
            val_2 = sum_stack.pop()
            result = ARITHMETIC_OPERATORS[val](val_1,val_2)
            sum_stack.push(result)
        else:
            if type(val) == float or type(val) == int:
                sum_stack.push(val)
    return sum_stack.pop()

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(False, False)
        default_font = ("Helvetica", "14")
        self.__current_num = tk.StringVar(self, "0")
        self.__numbers = []
        self.__operations = []

        self.wm_title("Calculator " + __version__)
        self.config(bg="#1c1c1c")
        self.__top_output = tk.Label(self, bg="#1c1c1c",fg="white")
        self.__output = tk.Label(
            self, textvariable=self.__current_num, bg="#1c1c1c",fg="white",
            relief="solid", anchor=tk.E, font=("Helvetica", "20"))
        b_clear = tk.Button(self, text="AC", font=default_font, command=self.bnt_clear)
        b_frame = tk.Frame(self)

        b_7 = tk.Button(b_frame, text="7", font=default_font, width=4, command=self.bnt_7)
        b_8 = tk.Button(b_frame, text="8", font=default_font, width=4, command=self.bnt_8)
        b_9 = tk.Button(b_frame, text="9", font=default_font, width=4, command=self.bnt_9)
        b_div = tk.Button(b_frame, text="/", font=default_font, width=4, command=self.bnt_div)
        b_floordiv = tk.Button(b_frame, text="//", font=default_font, width=4, command=self.bnt_floordiv)

        b_4 = tk.Button(b_frame, text="4", font=default_font, width=4, command=self.bnt_4)
        b_5 = tk.Button(b_frame, text="5", font=default_font, width=4, command=self.bnt_5)
        b_6 = tk.Button(b_frame, text="6", font=default_font, width=4, command=self.bnt_6)
        b_mult = tk.Button(b_frame, text="*", font=default_font, width=4, command=self.bnt_mult)
        b_power = tk.Button(b_frame, text="**", font=default_font, width=4, command=self.bnt_power)

        b_1 = tk.Button(b_frame, text="1", font=default_font, width=4, command=self.bnt_1)
        b_2 = tk.Button(b_frame, text="2", font=default_font, width=4, command=self.bnt_2)
        b_3 = tk.Button(b_frame, text="3", font=default_font, width=4, command=self.bnt_3)
        b_minus = tk.Button(b_frame, text="-", font=default_font, width=4, command=self.bnt_minus)
        b_perc = tk.Button(b_frame, text="%", font=default_font, width=4, command=self.bnt_perc)

        b_0 = tk.Button(b_frame, text="0", font=default_font, width=4, command=self.bnt_0)
        b_dot = tk.Button(b_frame, text=".", font=default_font, width=4, command=self.bnt_dot)
        b_equal = tk.Button(b_frame, text="=", font=default_font, width=9, command=self.bnt_equal)
        b_add = tk.Button(b_frame, text="+", font=default_font, width=4, command=self.bnt_add)


        b_7.grid(row=0, column=0)
        b_8.grid(row=0, column=1)
        b_9.grid(row=0, column=2)
        b_div.grid(row=0, column=3)
        b_floordiv.grid(row=0, column=4)

        b_4.grid(row=1, column=0)
        b_5.grid(row=1, column=1)
        b_6.grid(row=1, column=2)
        b_mult.grid(row=1, column=3)
        b_power.grid(row=1, column=4)

        b_1.grid(row=2, column=0)
        b_2.grid(row=2, column=1)
        b_3.grid(row=2, column=2)
        b_minus.grid(row=2, column=3)
        b_perc.grid(row=2, column=4)

        b_0.grid(row=3, column=0)
        b_dot.grid(row=3, column=1)
        b_equal.grid(row=3, column=2, columnspan=2)
        b_add.grid(row=3, column=4)

        self.__top_output.pack(fill=tk.X, padx=5)
        self.__output.pack(fill=tk.X, padx=5, pady=5)
        b_clear.pack(fill=tk.X, padx=5, pady=5)
        b_frame.pack(fill=tk.X, padx=5, pady=5)

        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())

    def add_to_current_num(self, value):
        if self.__current_num.get() == "0":
            if value != ".":
                self.__current_num.set("")
        self.__current_num.set(self.__current_num.get() + str(value))
        self.__output.config(text=self.__current_num.get())
    
    def bnt_clear(self):
        self.__current_num.set("0")
        self.__top_output.config(text="")
        self.__numbers = []
        self.__operations = []

    def bnt_7(self):
        self.add_to_current_num(7)
    def bnt_8(self):
        self.add_to_current_num(8)
    def bnt_9(self):
        self.add_to_current_num(9)
    def bnt_4(self):
        self.add_to_current_num(4)
    def bnt_5(self):
        self.add_to_current_num(5)
    def bnt_6(self):
        self.add_to_current_num(6)
    def bnt_1(self):
        self.add_to_current_num(1)
    def bnt_2(self):
        self.add_to_current_num(2)
    def bnt_3(self):
        self.add_to_current_num(3)
    def bnt_0(self):
        self.add_to_current_num(0)

    def bnt_dot(self):
        if not linear_search(self.__current_num.get(), "."):
            self.add_to_current_num(".")

    def bnt_equal(self):
        self.__numbers.append(float(self.__current_num.get()))
        self.__current_num.set("0")
        try:
            total = calculate_with_polish(self.__numbers, self.__operations)
            if total == int(total):
                total = int(total)
            self.__numbers = [total]
            self.__operations = []
            self.__current_num.set(str(total))
            self.__top_output.config(text="")
        except ZeroDivisionError:
            self.__top_output.config(text="Cannot divide by zero")
        except OverflowError:
            self.__top_output.config(text="Number to large")

    def __add_number_and_operation(self, operation):
        self.__numbers.append(float(self.__current_num.get()))
        self.__top_output.config(text=self.__current_num.get()+operation)
        self.__operations.append(operation)
        self.__current_num.set("0")

    def bnt_floordiv(self):
        self.__add_number_and_operation("//")
    def bnt_power(self):
        self.__add_number_and_operation("**")
    def bnt_perc(self):
        self.__current_num.set(str(float(self.__current_num.get()) / 100))
    def bnt_add(self):
        self.__add_number_and_operation("+")
    def bnt_minus(self):
        self.__add_number_and_operation("-")
    def bnt_mult(self):
        self.__add_number_and_operation("*")
    def bnt_div(self):
        self.__add_number_and_operation("/")


if __name__ == "__main__":
    root = Calculator()
    root.mainloop()
