import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import math
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

def set_tolerance(input_string):
    global tolerance
    toletance = Decimal(input_string)
    
def set_range(input_string):
    global range_begin
    global range_end 
    input_function.replace( " ", "" )
    separator = input_string.find("," , 0)
    range_begin = Decimal(input_string[0:separator])
    range_end = Decimal(input_string[separator+1, len(input_string)])
    

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

##################### WINDOW #############################################
root = Tk()
root.geometry("200x150")
 
frame = Frame(root)
frame.pack()
 
function_input = Entry(frame, width = 20)
function_input.insert(0,'')
function_input.pack(padx = 5, pady = 5)

tolerance_input = Entry(frame, width = 20)
tolerance_input.insert(0,'')
tolerance_input.pack(padx = 5, pady = 5)

range_input = Entry(frame, width = 20)
range_input.insert(0,'')
range_input.pack(padx = 5, pady = 5)
 
Button = Button(frame, text = "Submit", command = lambda: set_input_values(function_input.get(), 
                                                                           tolerance_input.get(), 
                                                                           range_input.get()
                                                                           ))
Button.pack(padx = 5, pady = 5)
root.mainloop()
#################### MATH BELOW ##########################################
answer = bisection()
print(" Bisection Method Gives Root At x =",answer)


shortcut = fsolve(f,[-1.5, 1.5])
print(" These are roots of function given with Fsolve ",shortcut)

x = np.linspace(-2,2,100)
plt.plot(x,f(x))
plt.grid()
plt.show()

