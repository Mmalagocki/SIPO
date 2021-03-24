import numpy as np
from tkinter import *

ta = 1
tb = 2
te = 0.1

################ GUI  ####################################
  
def set_values(ta, tb, te):
    set_right(tb)
    set_left(ta)
    set_epsylon(te)
    computeFibOpt()

def set_left(input_string):
    global ta
    ta = float(input_string)

def set_right(input_string):
    global tb
    tb = float(input_string)

def set_epsylon(input_string):
    global te
    te = float(input_string)

######### MATH ##################################
def calculateFmax(e,a,b):
    Fmax = int(2*(b-a)/e)
    return Fmax

def makeListFromFmax(Fmax):
    a = 0 # zerowy element
    b = 1 # pierwszy element
    t = 0 # element pomocniczy
    list = [a,b]

    while list[-1]<Fmax:
        t = b
        b = a+b
        a = t
        list.append(b)

    return list

def func(x):
    return (((-1)/(x-1)**2) * (np.log(x)-2*((x-1)/(x+1))))

def leftBound(a,b,N,i,list):
    return float((a + (list[N-i-1]/list[N-i+1]) * (b-a)))

def rightBound(a,b,N,i,list):
    return float((a + (list[N-i]/list[N-i+1]) * (b-a)))

def computeFibOpt():
    global ta
    global tb
    global te
    
    a = ta
    b = tb
    e = te
    Fmax = calculateFmax(e,a,b)
    listFibonacci = makeListFromFmax(Fmax)
    oN = len(listFibonacci)-2
	
	Label(frame, text= ("Optimal n = ", oN)).grid(row=9)
	
    i = float(1)

    #pierwsza iteracja
    x1 = leftBound(a,b,oN,i,listFibonacci)
    x2 = rightBound(a,b,oN,i,listFibonacci)  
    print(x1, x2)
    print(x2-x1)
    grid = 6
	
	fx1 = func(x1)
    fx2 = func(x2)

    while(abs(a-b)>e and i<=oN):
        i=i+1
        
        
        Label(frame, text="Processing:").grid(row = 5, column = 2)
        Label(frame, text= (" a = ", round(a, 2)) ).grid(row = grid, column = 2)
        Label(frame, text= (" b = ", round(b, 2)) ).grid(row = grid+1, column = 2)
        Label(frame, text= (" x1 = ", round(x1, 2)) ).grid(row = grid+2, column = 2)
        Label(frame, text= (" x2 = ", round(x2, 2)) ).grid(row = grid+3, column = 2)
        Label(frame, text= ("____________") ).grid(row = grid+4, column = 2)
        
        if(fx1 < fx2):
            a = a
            b = x2
            x2 = x1
			fx2 = fx1
            x1 = leftBound(a,b,oN,i,listFibonacci)
			fx1 = func(x1)
        elif (fx1 >= fx2):
            a = x1
            b = b
            x1 = x2
            x2 = rightBound(a,b,oN,i,listFibonacci)
			fx1 = fx2
			fx2 = func(x2)
        grid += 5
            
    Label(frame, text="Results:").grid(row=5)
    Label(frame, text= (" a = ", round(a, 2)) ).grid(row=6)
    Label(frame, text= (" b = ", round(b, 2)) ).grid(row=7)
    Label(frame, text= (" c = ", round(i, 2)) ).grid(row=8)
  
    return [a,b,i]

#print(func2(2.642))

root = Tk()
root.geometry("1000x600")
root.title("MM&MJ")

 
frame = Frame(root)

frame.pack()
### DISPLAYS CHOSEN VERSION
Label(frame, text="Fibonacci method").grid(row=0)

Label(frame, text="Left bound:").grid(row=1)
left_bound_input = Entry(frame, width = 20, cursor = 'hand2')
left_bound_input.insert(0,'')
left_bound_input.grid(row=1 , column=1, pady=10)

Label(frame, text="Right bound:").grid(row=2)
right_bound_input = Entry(frame, width = 20, cursor = 'hand2')
right_bound_input.insert(0,'')
right_bound_input.grid(row=2 , column=1, pady=10)

Label(frame, text="Epsylon:").grid(row=3)
input_epsylon = Entry(frame, width = 20, cursor = 'hand2')
input_epsylon.insert(0,'')
input_epsylon.grid(row=3 , column=1, pady=10)
 
Button_submit = Button(frame, text = "Submit", command = lambda: set_values(left_bound_input.get(),
                                                                            right_bound_input.get(),
                                                                            input_epsylon.get()
                                                                            ))
Button_submit.grid(row=4 , column=1)


root.mainloop()