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
def Fibonacci(n):
    if n<0:
        return "Incorrect argument"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def findNFromFib(fn):
    n = 2
    while(Fibonacci(n)<fn):
        n=n+1

    Label(frame, text="Optimal n:").grid(row=7, column = 1)
    Label(frame, text= n-1).grid(row=7, column = 2)
    return n-1

def findOptimalN(e,a,b):
    fn = int(2*(b-a)/e)
    return findNFromFib(fn)

def func(x):
    return (((-1)/(x-1)**2) * (np.log(x)-2*((x-1)/(x+1))))

def leftBound(a,b,N,i): 
    return float((a + (Fibonacci(N-i-1)/Fibonacci(N-i+1)) * (b-a)))

def rightBound(a,b,N,i):
    return float((a + (Fibonacci(N-i)/Fibonacci(N-i+1)) * (b-a)))

def computeFibOpt():
    global ta
    global tb
    global te
    
    a = ta
    b = tb
    e = te
    oN = float(findOptimalN(e,a,b))
    i = float(1)

    #pierwsza iteracja
    x1 = leftBound(a,b,oN,i)
    x2 = rightBound(a,b,oN,i)  
    print(x1, x2)
    print(x2-x1)

    while(abs(x1-x2)>e and i<=oN):
        i=i+1

        fx1 = func(x1)
        fx2 = func(x2)

        if(fx1 < fx2):
            a = a
            b = x2
            x2 = x1
            x1 = leftBound(a,b,oN,i)
        elif (fx1 >= fx2):
            a = x1
            b = b
            x1 = x2
            x2 = rightBound(a,b,oN,i)
            
    Label(frame, text="Results:").grid(row=5, column = 1)
    Label(frame, text= " a = ").grid(row=5, column = 2)
    Label(frame, text= " b = ").grid(row=5, column = 4)
    Label(frame, text= " c = ").grid(row=5, column = 6)
    Label(frame, text= a ).grid(row=5, column = 3)
    Label(frame, text= b ).grid(row=5, column = 5)
    Label(frame, text= i ).grid(row=5, column = 7)    
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