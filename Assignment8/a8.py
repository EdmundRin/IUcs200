###########################
# Problem One
###########################
# There is no unit testing 
# for this problem
###########################
import matplotlib.pyplot as plt
import random as rn
import math
import numpy as np # Missing Import

# translates a random int into a step along the random walk
# parameters: int i for the step index, numpy array x for tracking the left/right location at index i,
# numpy array y for tracking the forward/backward location at index i
# return: none
def step(x,y,i):
    
    # We have already setup the below line to return a list of four values
    # [1,2,3,4] out of which you will select the actions and act accordingly.
    # i.e., if you select 1 from direction below then move right and so on for other values.
    direction = rn.randint(1,4)
    # TODO: implement this function
    if direction == 1:
        x[i] = x[i] + 1
    elif direction == 2:
        x[i] = x[i] - 1
    elif direction == 3:
        y[i] = y[i] + 1
    elif direction == 4:
        y[i] = y[i] - 1
    else:
        print("Error: invalid direction")


# do not change code below for graphit() function.
# this function actually draws the plot that you see in the
# PDF. Your plot will be different from the one given in the 
# PDF due to the randomness in the walk.
def graphit(x,y,n):
   
    plt.title("Random {0} Walk\nLast Location {1},{2}".format(n,int(x[n-1]),int(y[n-1])) )
    plt.plot(x,y) 
    plt.plot([x[1],x[1]],[y[1]-10,y[1]+10], "b-")
    plt.plot([x[1]-10,x[1]+10],[y[1],y[1]], "b-")
    plt.plot([x[n-1]-10,x[n-1]+10],[y[n-1],y[n-1]], "r-")
    plt.plot([x[n-1],x[n-1]],[y[n-1]-10,y[n-1]+10], "r-")
    plt.show() 




###########################
# Problem Two
###########################

# input: 2 points in 2-dimensions example (1,2) or (3,4)
# output: the distance between them
def distance(p1, p2):
    from math import sqrt
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# input:  list of pairs, where each pair is a point in 2-dimensions
# output: [point1, point2, distane] where distance is the minimum out of all possible pair of points in xlst
# point1 is first point
# point2 is second point
# distance is the distance between the points
def brute(xlst):
    dist = distance(xlst[0], xlst[1])
    dist_list = [xlst[0],xlst[1],dist]
    for i in range(len(xlst)):
        for j in range(i+1, len(xlst)):
            if distance(xlst[i], xlst[j]) < dist:
                dist = distance(xlst[i], xlst[j])
                dist_list = [xlst[i], xlst[j], dist]
    return dist_list


###########################
# Problem Three
###########################

# input: N and time (set to 40)
# output: calculated productivity value

def productivity(N, T = 40):
    return N*T*(0.55-0.00005*N*(N-1))

""" 
Do Not Change the functions below.
All you have to do is to complete the productivity function above
The below functions are used to create the plot as shown in the PDF.
"""
def fp(f):
    h = .00001
    return lambda x: (f(x + h) - f(x-h))/(2*h)

def newton(f, fp, x, tau):
    def n(x):
        while f(x) > tau:
            x = x - f(x)/fp(x)
        return x
    return n(x)




###############
# PROBLEM Four
###############
# You CANNOT use ANY modules in this problem
###############

# input: a list of elements
# ouptut: a list of lists, where each sublist is a permutation of the original input list
def permutation(lst):
    if len(lst) == 1:
        return [lst]
    else:
        result = []
        for i in range(len(lst)):
            sublst = lst[:i] + lst[i+1:]
            for p in permutation(sublst):
                result.append([lst[i]] + p)
        return result


###############
# PROBLEM Five
###############

class Vector:
    def __init__(self, *x):
        self.__v = x

    def get_tuple(self):
        return self.__v

    def __add__(self,other):
        new = []
        for i in range(len(self.__v)):
            new.append(self.__v[i] + other.__v[i])
        if len(self.__v) < len(other.__v):
            for i in range(len(other.__v) - len(self.__v)):
                new.append(other.__v[i])
        return Vector(*new)

    def __sub__(self,other):
        new = []
        for i in range(len(self.__v)):
            new.append(self.__v[i] - other.__v[i])
        if len(self.__v) < len(other.__v):
            for i in range(len(other.__v) - len(self.__v)):
                new.append(-other.__v[i])
        return Vector(*new)

    def __rmul__(self,other): 
        # I'm not sure I understand this magic function and the next magic function correctly
        # Shouldn't the function of this one be included in the next one?
        new = []
        for i in range(len(self.__v)):
            new.append(self.__v[i] * other)
        return Vector(*new)

    def __mul__(self,other):
        if isinstance(other, Vector):
            result = 0
            for i in range(len(self.__v)):
                result += self.__v[i] * other.__v[i]
            return result
        else:
            new = []
            for i in range(len(self.__v)):
                new.append(self.__v[i] * other)
            return Vector(*new)

    def __abs__(self):
        result = 0
        for i in range(len(self.__v)):
            result += self.__v[i]**2
        return result**0.5

    def __neg__(self):
        new = []
        for i in range(len(self.__v)):
            new.append(-self.__v[i])
        return Vector(*new)

    def __eq__(self, other):
        if len(self.__v) != len(other.__v):
            return False
        for i in range(len(self.__v)):
            if self.__v[i] != other.__v[i]:
                return False
        return True

    def __repr__(self):
        return "<" + ",".join(map(str,self.__v)) + ">"




if __name__ == "__main__":

    # You are free to uncomment the below statements to test the code
    # but comment them back before submitting your final work.

# #PROBLEM 1
    #number of steps
    n = 100000   #You should change the number of steps to see
                 #to see how it affects the plot
    x = np.zeros(n) 
    y = np.zeros(n) 

    #fill array with step values 
    for i in range(1,n):
        step(x,y,i)

    graphit(x,y,n)

##PROBLEM 2
    x = [(rn.randint(1,50), rn.randint(1,50)) for _ in range(10)]
    print(x)
    print(brute(x))

##PROBLEM 3
    f = fp(productivity)
    x = math.ceil(newton(f,fp(f),62,.01))
    y = math.ceil(productivity(x))
 
    print("The maximum productivity is P({0}) ~ {1} person x hrs".format(x,y))

    t = np.arange(0.0, 100.0)
    fig,ax = plt.subplots()

    ax.plot(t, productivity(t),'g')
    ax.plot(x,productivity(x), 'bo--')
    ax.set(xlabel ="Number of people", ylabel="person x hrs", title = "Maximal Productivity P({0}) ~ {1}".format(x,y))

    ax.grid()
    plt.show()

## PROBLEM 4
    print(permutation([1,2,3]))
    print(permutation([1,2,3,4]))


## PROBLEM 5       
    x,y,w = Vector(1,2),Vector(3,-1),Vector(*(10,10))  
    z,a = Vector(0,3,2),Vector(-1,-1,-1) 
    print(x,y,z,a)
    print(x+y,z+a)
    print(x*y,z*a)
    print(5*x,5*z)
    print(abs(x),abs(z))
    print(-x,-z)
    print(x - y + y == x, 2 * z == z + z)