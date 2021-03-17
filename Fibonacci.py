import numpy as np

def Fibonacci(n):
    if n<0:
        return "Niepoprawny argument"
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

    print("Optymalne n: ", n-1)
    return n-1

def findOptimalN(e,a,b):
    fn = int(2*(b-a)/e)
    return findNFromFib(fn)

def func3(x):
    return (x**4 - 14*(x**3) + 60*(x**2) - 70*x)

def func(x):
    return (((-1)/(x-1)**2) * (np.log(x)-2*((x-1)/(x+1))))

def leftBound(a,b,N,i):
    return float((a + (Fibonacci(N-i-1)/Fibonacci(N-i+1)) * (b-a)))

def rightBound(a,b,N,i):
    return float((a + (Fibonacci(N-i)/Fibonacci(N-i+1)) * (b-a)))

def computeFibOpt(ta,tb,te):

    a = ta
    b = tb
    e = te
    oN = findOptimalN(e,a,b)
    i=1

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


    print("Koniec")
    print("a, b, i")
    return [a,b,i]


te = 0.001 #wstępnie niech epsilon = 0.1
ta = 1 # wstępnie a = 1
tb = 3 # wstępnie b = 2

print(computeFibOpt(ta,tb,te))
#print(func2(2.642))