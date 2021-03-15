import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import math
from scipy.optimize import fsolve 
   
input_function = ""
X_indexes = []
    
def find_xs(input_string):
    global input_function
    global X_indexes
    
    x_arrays = []
    first_x = input_string.find('x', 0)
    x_arrays.insert(0, first_x)
    i = 1
    while ((input_string.find( 'x', x_arrays[i-1] + 1) != -1) and (input_string.find( 'x', x_arrays[i-1] + 1) != None)):
        #print ("This is iteration of find_xs ",input_string.find( 'x', x_arrays[i-1] + 1 ))
        x_arrays.append(input_string.find( 'x', x_arrays[i-1] + 1 ))
        i += 1
        
    #print("This is first x position ", first_x)
    #print("This is array length ", len(x_arrays))
    X_indexes = x_arrays
    input_function = input_string
  

def f(x):
    global input_function
    global X_indexes
    
    input_function.replace("x", str(x) )
    input_function.replace( " ", "" )
    
    #print(input_function)
    code = compile(input_function, "<string>", "eval")
    return eval(code)

def bisection(a, b, tol):
    xl = a
    xr = b
    
    while (np.abs(xl-xr) >= tol):
        c = (xl + xr)/2.0
        prod = f(xl)*f(c)
        if prod > tol:
            xl = c
        else:
            if prod < tol:
                xr = c
    return c

##################### WINDOW #############################################
root = Tk()
root.geometry("200x150")
 
frame = Frame(root)
frame.pack()
 
my_entry = Entry(frame, width = 20)
my_entry.insert(0,'')
my_entry.pack(padx = 5, pady = 5)
 
Button = Button(frame, text = "Submit", command = lambda: find_xs(my_entry.get()))
Button.pack(padx = 5, pady = 5)
root.mainloop()
#################### MATH BELOW ##########################################
answer = bisection(-5,5,1e-8)
print(" Bisection Method Gives Root At x =",answer)


shortcut = fsolve(f,[-1.5, 1.5])
print(" These are roots of function given with Fsolve ",shortcut)

x = np.linspace(-2,2,100)
plt.plot(x,f(x))
plt.grid()
plt.show()

