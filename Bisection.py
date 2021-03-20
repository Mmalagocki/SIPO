import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
from tkinter import *
from scipy.optimize import fsolve 
from decimal import Decimal
   
input_function = ""
X_indexes = []
tolerance = ""
range_begin = ""
range_end = ""

################################# INPUT FUNCTIONS ##################################################################
def set_input_values(function, tolerance, range_dimm):
    set_tolerance(tolerance)
    find_xs(function)
    set_range(range_dimm)
    math_stuff()

def set_tolerance(input_string):
    global tolerance
    tolerance = float(input_string)
    
def set_range(input_string):
    global range_begin
    global range_end 
    input_function.replace( " ", "" )
    separator = input_string.find("," , 0)
    range_begin = float(input_string[0:separator])
    range_end = float(input_string[separator+1:])
    

def find_xs(input_string):
    global input_function
    global X_indexes
    x_arrays = []
    first_x = input_string.find('x', 0)
    x_arrays.insert(0, first_x)
    i = 1
    
    while ((input_string.find( 'x', x_arrays[i-1] + 1) != -1) and (input_string.find( 'x', x_arrays[i-1] + 1) != None)):
        x_arrays.append(input_string.find( 'x', x_arrays[i-1] + 1 ))
        i += 1
        
    X_indexes = x_arrays
    input_function = input_string
  
################## MATH FUNCTIONS ###########################################################
def f(x):
    global input_function
    global X_indexes
    
    input_function.replace( "x", str(x) )
    input_function.replace( " ", "" )
    code = compile(input_function, "<string>", "eval")
    return eval(code)

def bisection():
    global tolerance
    global range_begin
    global range_end    

    while (np.abs(range_begin-range_end) >= tolerance):
        c = (range_begin + range_end)/2.0
        prod = f(range_begin)*f(c)
        if prod > tolerance:
            range_begin = c
        else:
            if prod < tolerance:
                range_end = c
    return c
def math_stuff():
    global range_begin
    global range_end
    answer = bisection()
    Label(frame, text="Answer:").grid(row=5)
    Label(frame, text=answer).grid(row=5, column = 1)
    #print(" Bisection Method Gives Root At x =",answer)
    
    
    shortcut = fsolve(f,[range_begin, range_end])
    print(" These are roots of function given with Fsolve ",shortcut)
    
    Label(frame, text="Shortcut:").grid(row=6)
    Label(frame, text=shortcut).grid(row=6, column = 1)    
 
    x = np.linspace(range_begin,range_end,100)
    plt.plot(x,f(x))
    plt.grid()  
    plt.show()    

##################### WINDOW #############################################
root = Tk()
root.geometry("600x600")
root.title("MM&MJ")

 
frame = Frame(root)
frame.pack()

Label(frame, text="First exercise").grid(row=0)

Label(frame, text="Function:").grid(row=1)
function_input = Entry(frame, width = 20, cursor = 'hand2')
function_input.insert(0,'')
function_input.grid(row=1 , column=1, pady=10)

Label(frame, text="Tolerance:").grid(row=2)
tolerance_input = Entry(frame, width = 20, cursor = 'hand2')
tolerance_input.insert(0,'')
tolerance_input.grid(row=2 , column=1, pady=10)

Label(frame, text="Range in form (2,2):").grid(row=3)
range_input = Entry(frame, width = 20, cursor = 'hand2')
range_input.insert(0,'')
range_input.grid(row=3 , column=1, pady=10)
 
Button = Button(frame, text = "Submit", command = lambda: set_input_values(function_input.get(), 
                                                                           tolerance_input.get(), 
                                                                           range_input.get()
                                                                           ))
Button.grid(row=4 , column=1)


root.mainloop()
#################### MATH BELOW ##########################################


