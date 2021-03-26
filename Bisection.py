import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
from tkinter import *
from scipy.optimize import fsolve
   
input_function = ""
tolerance = ""
range_begin = ""
range_end = ""
iterations = ""
results_array_len = 2
results = []

################################# INPUT FUNCTIONS ##################################################################

def iterations_chosen():
    Label(frame, text="You have chosen iterations").grid(row = 0)
    
    Label(frame, text="Function:").grid(row = 1)
    function_input = Entry(frame, width = 20, cursor = 'hand2')
    function_input.insert(0,'')
    function_input.grid(row=1 , column=1, pady = 10)
    
    Label(frame, text="Iterations:").grid(row = 2)
    iterations_input = Entry(frame, width = 20, cursor = 'hand2')
    iterations_input.insert(0,'')
    iterations_input.grid(row = 2 , column=1, pady = 10)
    
    Label(frame, text="Range in form (2,2):").grid(row = 3)
    range_input = Entry(frame, width = 20, cursor = 'hand2')
    range_input.insert(0,'')
    range_input.grid(row = 3 , column = 1, pady = 10)
     
    Button_submit = Button(frame, text = "Submit", command = lambda: set_iterations_values(function_input.get(), 
                                                                               iterations_input.get(), 
                                                                               range_input.get()
                                                                               ))
    Button_submit.grid(row=4 , column=1)

def tolerance_chosen():
    Label(frame, text="You have chosen tolerance").grid(row = 0)
    
    Label(frame, text="Function:").grid(row = 1)
    function_input = Entry(frame, width = 20, cursor = 'hand2')
    function_input.insert(0,'')
    function_input.grid(row=  1 , column = 1, pady = 10)
    
    Label(frame, text="Tolerance:").grid(row = 2)
    tolerance_input = Entry(frame, width = 20, cursor = 'hand2')
    tolerance_input.insert(0,'')
    tolerance_input.grid(row = 2 , column = 1, pady = 10)
    
    Label(frame, text="Range in form ( -2,2 ):").grid(row = 3)
    range_input = Entry(frame, width = 20, cursor = 'hand2')
    range_input.insert(0,'')
    range_input.grid(row = 3 , column = 1, pady = 10)
     
    Button_submit = Button(frame, text = "Submit", command = lambda: set_tolerance_values(function_input.get(), 
                                                                               tolerance_input.get(), 
                                                                               range_input.get()
                                                                               ))
    Button_submit.grid(row = 4 , column = 1)

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
def not_unimodal_bisection(range_begin, range_end):
    global iterations
    global tolerance
    global results_array_len
    global results
        
    if(iterations != ""):
        distance = np.abs(range_begin-range_end) 
        while (i  < iterations):
            delta = distance / 4
            cl = 0.5 * (range_begin + range_end) - delta
            cr = 0.5 * (range_begin + range_end) + delta               
            #c = (range_begin + range_end)/2.0
            prod = f(range_begin)*f(c)
            Label(frame, text = "Processing ").grid(row = 5, column = 2 )
            Label(frame, text =  i).grid(row = grid + 3, column = column)
            Label(frame, text = "Range begin: ").grid(row = grid, column = column)
            Label(frame, text = round(range_begin,2)).grid(row = grid + 1, column = column)
            Label(frame, text = "Range end: ").grid(row = grid, column = column + 1)
            Label(frame, text = round(range_end,2)).grid(row = grid + 1, column = column + 1)    
            Label(frame, text = "___________").grid(row = grid + 2, column = column + 1)
            Label(frame, text = "___________").grid(row = grid + 2, column = column)
            ##print ("range_begin ", (range_begin), " range_end ", str(range_end))
            if ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) <= f(cr))) :
                print ("1")
                range_begin = cl
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) >= f(cr))) :
                print ("2")
                range_begin =  cl
            elif ((f(range_begin) <= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) >= f(cr))):
                print ("3")
                range_begin = cl    
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) >= f(cr))):
                print ("4")
                range_begin = cl
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) <= f(cr))):
                print ("5")
                range_end = cr
            elif ((f(range_begin) <= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) <= f(cr))):
                print ("6")
                range_end = cr                    
            elif (f(range_end) < f(cl)) and (f(cr) > f(range_begin)):
                print ("7")
                not_unimodal_bisection(range_begin, cl)
                not_unimodal_bisection(cr, range_end)
                not_unimodal_bisection(cl, cr)
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) < f(range_end)) and (f(cl) <= f(cr))):
                print ("8")
                range_begin = cl              
            else:
                print('Im going into else!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                if(f(range_begin) >= f(cl)):
                    print('f(range_begin) >= f(cl)')
                else:
                    print('f(range_begin) < f(cl)')
                if(f(range_begin) >= f(range_end)):
                    print('f(range_begin) >= f(range_end)')
                else:
                    print('f(range_begin) < f(range_end)')
                if(f(cl) <= f(cr)):
                    print('f(cl) <= f(cr)')
                else:
                    print('f(cl) > f(cr)')
                
                print('That is how far i go')
                if(f(range_begin) <= f(cr)):
                    print('f(range_begin) <= f(cr)')
                else:
                    print('f(range_begin) > f(cr)')
                if(f(range_end) <= f(cr)):
                    print('f(range_end) <= f(cr)')
                else:
                    print('f(range_end) > f(cr)')          
                if(f(range_end) >= f(cl)):
                    print('f(range_end) >= f(cl)')
                else:
                    print('f(range_end) < f(cl)')        
                if(f(range_end) >= f(cl)):
                    print('f(range_end) >= f(cl)')
                else:
                    print('f(range_end) < f(cl)')    
                print('I reach here')
                return 0
            i+= 1
            if(grid <= 13):
                grid += 4
            else:
                grid = 7
                column += 5 
        
            results_array_len += 1
            results.insert(results_array_len, range_begin)
            results_array_len += 1
            results.insert(results_array_len, range_end)
            
    else:
        distance = np.abs(range_begin-range_end) 
        while (distance >= tolerance):

            #print ("Beging", range_begin, "end", range_end)
            #print ("Distance", distance, )
            delta = distance/ 4
            cl = 0.5 * (range_begin + range_end) - delta
            cr = 0.5 * (range_begin + range_end) + delta               
            Label(frame, text = "Processing ").grid(row = 5, column = 2 )
            Label(frame, text =  i).grid(row = grid + 3, column = column)
            Label(frame, text = "Range begin: ").grid(row = grid, column = column)
            Label(frame, text = round(range_begin,2)).grid(row = grid + 1, column = column)
            Label(frame, text = "Range end: ").grid(row = grid, column = column + 1)
            Label(frame, text = round(range_end,2)).grid(row = grid + 1, column = column + 1)    
            Label(frame, text = "___________").grid(row = grid + 2, column = column + 1)
            Label(frame, text = "___________").grid(row = grid + 2, column = column)
            ##print ("range_begin ", (range_begin), " range_end ", str(range_end))
            if ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) <= f(cr))) :
                print ("1")
                range_begin = cl
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) >= f(cr))) :
                print ("2")
                range_begin =  cl
            elif ((f(range_begin) <= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) >= f(cr))):
                print ("3")
                range_begin = cl    
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) >= f(cr))):
                print ("4")
                range_begin = cl
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) <= f(cr))):
                print ("5")
                range_end = cr
            elif ((f(range_begin) <= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) <= f(cr))):
                print ("6")
                range_end = cr                    
            elif (f(range_end) < f(cl)) and (f(cr) > f(range_begin)):
                print ("7")
                not_unimodal_bisection(range_begin, cl)
                not_unimodal_bisection(cr, range_end)
                not_unimodal_bisection(cl, cr)
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) < f(range_end)) and (f(cl) <= f(cr))):
                print ("8")
                range_begin = cl              
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) < f(range_end)) and (f(cl) > f(cr))):
                print ("9")
                range_end = cr                    
            else:
                print('Im going into else!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                if(f(range_begin) >= f(cl)):
                    print('f(range_begin) >= f(cl)')
                else:
                    print('f(range_begin) < f(cl)')
                if(f(range_begin) >= f(range_end)):
                    print('f(range_begin) >= f(range_end)')
                else:
                    print('f(range_begin) < f(range_end)')
                if(f(cl) <= f(cr)):
                    print('f(cl) <= f(cr)')
                else:
                    print('f(cl) > f(cr)')
                
                print('That is how far i go')
                if(f(range_begin) <= f(cr)):
                    print('f(range_begin) <= f(cr)')
                else:
                    print('f(range_begin) > f(cr)')
                if(f(range_end) <= f(cr)):
                    print('f(range_end) <= f(cr)')
                else:
                    print('f(range_end) > f(cr)')          
                if(f(range_end) >= f(cl)):
                    print('f(range_end) >= f(cl)')
                else:
                    print('f(range_end) < f(cl)')        
                if(f(range_end) >= f(cl)):
                    print('f(range_end) >= f(cl)')
                else:
                    print('f(range_end) < f(cl)')    
                print('I reach here')
                return 0

            i+=1
            distance = np.abs(range_begin-range_end)
            if(grid <= 13):
                grid += 4
            elif(column < 14):
                grid = 7
                column += 5                
            else:
                continue
            
        results_array_len += 1
        results.insert(results_array_len, range_begin)
        results_array_len += 1
        results.insert(results_array_len, range_end)
    

def bisection():
    global tolerance
    global range_begin
    global range_end
    global results
    global iterations
    i = 0
    grid = 7
    column = 2

    
    if(iterations != ""):
        distance = np.abs(range_begin-range_end) 
        while (i  < iterations):
            delta = distance / 4
            cl = 0.5 * (range_begin + range_end) - delta
            cr = 0.5 * (range_begin + range_end) + delta               
            #c = (range_begin + range_end)/2.0
            prod = f(range_begin)*f(c)
            Label(frame, text = "Processing ").grid(row = 5, column = 2 )
            Label(frame, text =  i).grid(row = grid + 3, column = column)
            Label(frame, text = "Range begin: ").grid(row = grid, column = column)
            Label(frame, text = round(range_begin,2)).grid(row = grid + 1, column = column)
            Label(frame, text = "Range end: ").grid(row = grid, column = column + 1)
            Label(frame, text = round(range_end,2)).grid(row = grid + 1, column = column + 1)    
            Label(frame, text = "___________").grid(row = grid + 2, column = column + 1)
            Label(frame, text = "___________").grid(row = grid + 2, column = column)
            ##print ("range_begin ", (range_begin), " range_end ", str(range_end))
            if ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) <= f(cr))) :
                print ("1")
                range_begin = cl
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) >= f(cr))) :
                print ("2")
                range_begin =  cl
            elif ((f(range_begin) <= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) >= f(cr))):
                print ("3")
                range_begin = cl    
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) >= f(cr))):
                print ("4")
                range_begin = cl
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) <= f(cr))):
                print ("5")
                range_end = cr
            elif ((f(range_begin) <= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) <= f(cr))):
                print ("6")
                range_end = cr                    
            elif (f(range_end) < f(cl)) and (f(cr) > f(range_begin)):
                print ("7")
                not_unimodal_bisection(range_begin, cl)
                not_unimodal_bisection(cr, range_end)
                not_unimodal_bisection(cl, cr)
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) < f(range_end)) and (f(cl) <= f(cr))):
                print ("8")
                range_begin = cl              
            else:
                print('Im going into else')
                if(f(range_begin) >= f(cl)):
                    print('f(range_begin) >= f(cl)')
                else:
                    print('f(range_begin) < f(cl)')
                if(f(range_begin) >= f(range_end)):
                    print('f(range_begin) >= f(range_end)')
                else:
                    print('f(range_begin) < f(range_end)')
                if(f(cl) <= f(cr)):
                    print('f(cl) <= f(cr)')
                else:
                    print('f(cl) > f(cr)')
            i+= 1
            if(grid <= 13):
                grid += 4
            else:
                grid = 7
                column += 5
                
        results.insert(1, range_begin)
        results.insert(2, range_end)
        j = 1
        grid = 6
        
        if( len(results) > 3):
            while (j <= len(results)):
                print ("I'm working2")
                print (len(results))
                Label(frame, text = ( results[j], results[j+1])).grid(row = grid)
                j += 2
                grid += 2
            return "There was many results"
        return  range_begin, range_end
    
    else:
        distance = np.abs(range_begin-range_end) 
        while (distance >= tolerance):
             
            #print ("Beging", range_begin, "end", range_end)
            #print ("Distance", distance, )
            delta = distance/ 4
            cl = 0.5 * (range_begin + range_end) - delta
            cr = 0.5 * (range_begin + range_end) + delta               
            Label(frame, text = "Processing ").grid(row = 5, column = 2 )
            Label(frame, text =  i).grid(row = grid + 3, column = column)
            Label(frame, text = "Range begin: ").grid(row = grid, column = column)
            Label(frame, text = round(range_begin,2)).grid(row = grid + 1, column = column)
            Label(frame, text = "Range end: ").grid(row = grid, column = column + 1)
            Label(frame, text = round(range_end,2)).grid(row = grid + 1, column = column + 1)    
            Label(frame, text = "___________").grid(row = grid + 2, column = column + 1)
            Label(frame, text = "___________").grid(row = grid + 2, column = column)
            ##print ("range_begin ", (range_begin), " range_end ", str(range_end))
            if ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) <= f(cr))) :
                print ("1")
                range_begin = cl
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) >= f(cr))) :
                print ("2")
                range_begin =  cl
            elif ((f(range_begin) <= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) >= f(cr))):
                print ("3")
                range_begin = cl    
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) >= f(range_end)) and (f(cl) >= f(cr))):
                print ("4")
                range_begin = cl
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) <= f(cr))):
                print ("5")
                range_end = cr
            elif ((f(range_begin) <= f(cl)) and (f(range_begin) <= f(range_end)) and (f(cl) <= f(cr))):
                print ("6")
                range_end = cr                    
            elif (f(range_end) < f(cl)) and (f(cr) > f(range_begin)):
                print ("7")
                not_unimodal_bisection(range_begin, cl)
                not_unimodal_bisection(cr, range_end)
                not_unimodal_bisection(cl, cr)
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) < f(range_end)) and (f(cl) <= f(cr))):
                print ("8")
                range_begin = cl     
            elif ((f(range_begin) >= f(cl)) and (f(range_begin) < f(range_end)) and (f(cl) > f(cr))):
                print ("9")
                range_end = cr                            
            else:
                print('Im going into else!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                if(f(range_begin) >= f(cl)):
                    print('f(range_begin) >= f(cl)')
                else:
                    print('f(range_begin) < f(cl)')
                if(f(range_begin) >= f(range_end)):
                    print('f(range_begin) >= f(range_end)')
                else:
                    print('f(range_begin) < f(range_end)')
                if(f(cl) <= f(cr)):
                    print('f(cl) <= f(cr)')
                else:
                    print('f(cl) > f(cr)')
                if(f(range_begin) <= f(cr)):
                    print('f(range_begin) <= f(cr)')
                else:
                    print('f(range_begin) > f(cr)')
                if(f(range_end) <= f(cr)):
                    print('f(range_end) <= f(cr)')
                else:
                    print('f(range_end) > f(cr)')          
                if(f(range_end) >= f(cl)):
                    print('f(range_end) >= f(cl)')
                else:
                    print('f(range_end) < f(cl)')        
                if(f(range_end) >= f(cl)):
                    print('f(range_end) >= f(cl)')
                else:
                    print('f(range_end) < f(cl)')    
                print('I reach here')
                return 0

            i+=1
            distance = np.abs(range_begin-range_end)
            if(grid <= 13):
                grid += 4
            elif(column < 14):
                grid = 7
                column += 5                
            else:
                continue
        
        results.insert(0, range_begin)
        results.insert(1, range_end)
        j = 0
        grid = 6
        
        if( len(results) > 3):
            while (j <= len(results)):
                print ("I'm working2")
                print (len(results))
                Label(frame, text = ( results[j], results[j+1])).grid(row = grid)
                j += 2
                grid += 2
            return "There was many results"
        return  range_begin, range_end

def math_stuff():
    global range_begin
    global range_end
 
    initial_begin = range_begin
    initial_end = range_end
    
    answer = bisection()
    Label(frame, text=("Answer:", answer)).grid(row=5)
    #Label(frame, text=answer).grid(row=5, column = 1)
    #print(" Bisection Method Gives Root At x =",answer)
    
    shortcut = fsolve(f,[range_begin, range_end])    
    Label(frame, text=("Fsolve result:", shortcut)).grid(row=6)
    #bel(frame, text=shortcut).grid(row=6, column = 1)    
    x = np.linspace(initial_begin,initial_end,100)
    plt.plot(x,f(x))
    plt.grid()  
    plt.show()    

##################### WINDOW #############################################
root = Tk()
root.geometry("1200x900")
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


