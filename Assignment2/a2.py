import math

#problem 1
#input real
#return real
def g(x):
    if x == 0:
        return 1
    elif x == 1:
        return 2
    else:
        return x + 2


#problem 2
#input year 1977-1997
#return percent income or "error: year" if year 
#is outside range
def f(t):
    if 1977 <= t <= 1997:
        if 1977 <= t <= 1984:
            return (2/7)*(t-1977)+12
        elif 1984 < t <= 1987:
            return (t-1977)+7
        else:
            return (3/5)*(t-1977)+11
    else:
        return "error: year"


#problem 3
#input t years = 0
#output dollars
def h_0(t):
    return 110/((1/2)*t+1)

def h_1(t):
    return 26* ((1/4)*t**2-1)**2 +52

def h(t):
    return h_0(t) - h_1(t)


#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def q(coefficients):
    from math import sqrt 
    a,b,c = coefficients
    delta = b**2 - 4 * a* c 
    r1 = (-b + sqrt (delta) )/(2*a)
    r2 = (-b - sqrt (delta) )/(2*a)
    return (r1,r2)


#problem 5
#input [arg1,op,arg2,ans]
#output arg1 op arg2 == ans
def eq(lst):
    arg1,op,arg2,ans = lst
    if op == "+":
        result = arg1 + arg2
    elif op == "-":
        result = arg1 - arg2
    elif op == "*":
        result = arg1 * arg2
    elif op == "/":
        result = arg1 / arg2 
    else:
        return "error input"
    if result == ans:
        return True
    else:
        return False 



#problem 6
#input list of swithes
#output True if path from start to end
def path(lst):
    s0,s1,s2,s3,s4 = lst
    if s0 == 1 and s2 == 1 :
        return True
    elif s0 == 1 and s1 == 1 and (s3 or s4) == 1 :
        return True 
    else:
        return False 

#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
def max2d(x,y):
    if x >= y:
        return x 
    elif x < y:
        return y 
    else:
        print("Please enter the correct parameters")

#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x,y,z):
    r1 = max2d(x,y)
    return max2d(r1,z)


#from homework
def m(x,y):
    return (x > y)*x + (x <= y)*y

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

    #problem 1 
print(g(0))
print(g(1))
print(g(1.01))

    #problem 2
print(f(1976))
print(f(1977))
print(f(1985))
print(f(1988))
print(f(2000))

    #problem 3
print(h(0))
print(h(1))
print(h(2))

    #problem 4
print(q((1,0,-1)))
print(q((6,-1,-35)))
print(q((1,-7,-7)))

    #problem 5
print(eq([14, "/",2, 7]))
print(eq([20, "*",19, 381]))
print(eq([20, "*",19, 380]))

    #problem 6
print(path([1,0,1,0,0]))
print(path([1,1,1,0,0]))
print(path([1,0,0,1,0]))

    #problem 7
print(max3d(1,2,3))
print(max3d(1,3,2))
print(max3d(3,2,1))
print(max3d(3,3,1))
print(max3d(3,3,3))
print(max3d(1,2,2))