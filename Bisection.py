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
tolerance = ""
range_begin = ""
range_end = ""
iterations = ""

################################# INPUT FUNCTIONS ##################################################################

def iterations_chosen():
    Label(frame, text="You have chosen tolerance").grid(row=0)
    
    Label(frame, text="Function:").grid(row=1)
    function_input = Entry(frame, width = 20, cursor = 'hand2')
    function_input.insert(0,'')
    function_input.grid(row=1 , column=1, pady=10)
    
    Label(frame, text="Iterations:").grid(row=2)
    iterations_input = Entry(frame, width = 20, cursor = 'hand2')
    iterations_input.insert(0,'')
    iterations_input.grid(row=2 , column=1, pady=10)
    
    Label(frame, text="Range in form (2,2):").grid(row=3)
    range_input = Entry(frame, width = 20, cursor = 'hand2')
    range_input.insert(0,'')
    range_input.grid(row=3 , column=1, pady=10)
     
    Button_submit = Button(frame, text = "Submit", command = lambda: set_iterations_values(function_input.get(), 
                                                                               iterations_input.get(), 
                                                                               range_input.get()
                                                                               ))
    Button_submit.grid(row=4 , column=1)

def tolerance_chosen():
    Label(frame, text="You have chosen iterations").grid(row=0)
    
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
     
    Button_submit = Button(frame, text = "Submit", command = lambda: set_tolerance_values(function_input.get(), 
                                                                               tolerance_input.get(), 
                                                                               range_input.get()
                                                                               ))
    Button_submit.grid(row=4 , column=1)

def choose_main_condition(chosen_condition):
    if (chosen_condition == "Get the result based on  tolerance") :
        tolerance_chosen()
    elif(chosen_condition == "Get the result based on  number of iterations"):
        iterations_chosen()
    else:
        something_went_wront(chosen_condition)

def something_went_wront(chosen_condition):
    Label(frame, text="Sorry! Something went wrong. Here is the codition: " + chosen_condition).grid(row=0)


def set_tolerance_values(function, tolerance, range_dimm):
    set_tolerance(tolerance)
    set_function(function)
    set_range(range_dimm)
    math_stuff()

def set_iterations_values(function, iterations, range_dimm):
    set_iterations(iterations)
    set_function(function)
    set_tolerance(0.0001)
    set_range(range_dimm)
    math_stuff()    

def set_tolerance(input_string):
    global tolerance
    tolerance = float(input_string)
    
def set_function(input_string):
    global input_function
    input_function = input_string

def set_range(input_string):
    global range_begin
    global range_end 
    input_function.replace( " ", "" )
    separator = input_string.find("," , 0)
    range_begin = float(input_string[0:separator])
    range_end = float(input_string[separator+1:])

def set_iterations(input_string):
    global iterations
    iterations = float(input_string)    
  
################## MATH FUNCTIONS ###########################################################
def f(x):
    global input_function
    
    input_function.replace( "x", str(x) )
    input_function.replace( " ", "" )
    code = compile(input_function, "<string>", "eval")
    return eval(code)

def bisection():
    global tolerance
    global range_begin
    global range_end
    global iterations
    i = 0
    grid = 7
    
    if(iterations != ""):
        while (i  < iterations):
            c = (range_begin + range_end)/2.0
            prod = f(range_begin)*f(c)
            Label(frame, text="Range begin: ").grid(row=grid, column = 1)
            Label(frame, text=range_begin).grid(row=grid + 1, column = 1)
            Label(frame, text="Range end: ").grid(row=grid, column = 2)
            Label(frame, text=range_begin).grid(row=grid + 1, column = 2)            
            ##print ("range_begin ", (range_begin), " range_end ", str(range_end))
            if prod > tolerance:
                range_begin = c
            else:
                if prod < tolerance:
                    range_end = c
            i+= 1
            grid += 2
            
        
        return c        
    else:
        while (np.abs(range_begin-range_end) >= tolerance):
            c = (range_begin + range_end)/2.0
            prod = f(range_begin)*f(c)
            Label(frame, text="Range begin: ").grid(row=grid, column = 1)
            Label(frame, text=range_begin).grid(row=grid + 1, column = 1)
            Label(frame, text="Range end: ").grid(row=grid, column = 2)
            Label(frame, text=range_end).grid(row=grid + 1, column = 2)              
            ##print ("range_begin ", (range_begin), " range_end ", str(range_end))
            if prod > tolerance:
                range_begin = c
            else:
                if prod < tolerance:
                    range_end = c
            grid += 2
        return c        

def math_stuff():
    global range_begin
    global range_end
    answer = bisection()
    Label(frame, text="Answer:").grid(row=5)
    Label(frame, text=answer).grid(row=5, column = 1)
    #print(" Bisection Method Gives Root At x =",answer)
    
    
    shortcut = fsolve(f,[range_begin, range_end])    
    Label(frame, text="Fsolve result:").grid(row=6)
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
B = Button(root, text = "Choose condition", command = lambda: choose_main_condition(tkvarq.get()) )

options = ["Get the result based on  tolerance",
           "Get the result based on  number of iterations"
           ]

## SELECT MENU
tkvarq = StringVar(root)
tkvarq.set(options[0])
question_menu = OptionMenu(root, tkvarq, *options)
question_menu.pack()
B.pack()
frame.pack()
### DISPLAYS CHOSEN VERSION



root.mainloop()
#################### MATH BELOW ##########################################


