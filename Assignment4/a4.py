import math
from turtle import pen

###########################################################################
# Functions for Problem 1
###########################################################################
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}

def a(dlst):
    d,m,y = dlst 
    result = y - (14-m)/12
    return result 
def b(dlst):
    from math import floor 
    result = a(dlst) + a(dlst)/4 - a(dlst)/100 + a(dlst)/400
    return floor(result) 

def c(dlst):
    d,m,y = dlst 
    return m + 12*((14-m)/12) -2 
    

# INPUT dlst = [d,m,y]
# RETURN day the week that the given date falls on
def day(dlst):
    d,m,y = dlst 
    result = (d + b(dlst) + 31* (c(dlst)/12)) %7
    day = week.get(result)
    return day 


###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
def q(t):
    from math import sqrt 
    a,b,c = t
    delta = b**2 - 4*a*c
    if  delta >= 0:
        r0 = (-b +sqrt (delta)) / (2*a)
        r1 = (-b -sqrt (delta)) / (2*a)
        return (round(r1,2),round(r0,2)) 
    elif delta < 0:
        c0 = complex(round(-b/(2*a),2) , round(sqrt(-delta)/(2*a),2))
        c1 = complex(round(-b/(2*a),2) , round(-sqrt(-delta)/(2*a),2))
        return (c0,c1)
    else:
        return "No root"

###########################################################################
# Functions for Problem 3
###########################################################################
def inner_prod(v0,v1):
    sum = 0
    for i in range(len(v0)) :
        sum += v0[i] * v1[i]
    return sum 


def mag(v):
    from math import sqrt 
    return sqrt(inner_prod(v,v))

def angle(v0,v1):
    from math import pi, acos
    return round( (180/pi)*acos(inner_prod(v0,v1)/(mag(v0)*mag(v1))), 2)

def match(people):
    result = []
    for i in range(len(people)):
        for j in range(i,len(people)):
            if i != j:
                # debug: print(i,j)
                result += [[people[i],people[j],angle(people[i],people[j])]]
                continue
            else:
                pass
    return result 

def best_match(scores):
    # oldVersion:
    # dict = {}
    # for item in scores:
    #     a,b,c = item
    #     dict[c] = item 
        # print(dict)
    # mini = min(dict.keys())
    # for key,value in dict.items():
        # if key == mini:
            # return tuple(value)
    # New:
    # debug: print(scores[0][2])
    theta = scores[0][2]
    mini = scores[0]
    for i in range (len(scores)):   
        if scores[i][2] < theta:
            theta = scores[i][2]
            mini = tuple(scores[i])
    return mini


###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT 
#RETURN 
def intersect(d0,d1):
    m0,c0 = d0
    m1,c1 = d1 
    if m0 != m1:
        x = round((c1-c0)/(m0-m1),2)
        y = round(m0*x+c0,2)
        return (x,y)
    else:
        return "They are parallel"



###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message
def mean(lst):
    sum = 0
    if len(lst) != 0:
        for item in lst:
            sum += item
        return round(sum / len (lst),2)
    else:
        return "error"

def variance(lst):
    if len(lst) != 0:
        x = mean(lst)
        sum = 0
        for item in lst:
            sum += (item - x)**2
        return round(sum / len(lst),2)
    else:
        return "error"


def std(lst):
    from math import sqrt
    if len(lst) != 0:
        return round(sqrt (variance(lst)),2)
    else:
        return "error"

def mean_centered(lst):
    newlst = []
    if len(lst) != 0:
        for item in lst:
            newlst += [item - mean(lst),]
        return newlst
    else:
        return "error"


###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT x filters
#RETURN fixed cost
def equi(s,d):
    from math import sqrt 
    a1,b1,c1 = s 
    a2,b2,c2 = d 
    f1 = (b1-b2)**2+4*(a1-a2)*(c2-c1)
    if f1 >= 0:
        x1 = -(b1-b2)/(2*(a1-a2)) + sqrt(f1)/(2*(a1-a2))
        x2 = -(b1-b2)/(2*(a1-a2)) - sqrt(f1)/(2*(a1-a2))
        return (round(x2,2),round(x1,2))
    elif f1 < 0:
        x1 = complex(round(-(b1-b2)/(2*(a1-a2)),2), round (sqrt(-f1)/(2*(a1-a2)),2))
        x2 = complex(round(-(b1-b2)/(2*(a1-a2)),2), round (-sqrt(-f1)/(2*(a1-a2)),2))
        return (x1,x2)
    else:
        return "No result"   

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You can uncomment the below print statements to test you code
    but __remember__ to comment them before submitting the final version.

    Note: Do not leave print statements outside the body of the functions.
    All print statements must be commented after you are done testing your
    code and before pushing the final version of your HW.
    """

    # #problem 1
    print(day([14,2,2000]))
    print(day([14,2,1963]))
    print(day([14,2,1972]))

    #problem 2
    print(q((3,4,2)))
    print(q((1,3,-4)))
    print(q((1,-2,-4)))

    # #problem 3
    people0 = [[0,1,1],[1,0,0],[1,1,1]]
    print(match(people0))
    print(best_match(match(people0)))

    people = [[0,0,1],[1,0,0],[1,1,1]]
    print(match(people))
    print(best_match(match(people)))


    people1 = [[0,1,1,0,0,0,1],
               [1,1,0,1,1,1,0],
               [1,0,1,1,0,1,1],
               [1,0,0,1,1,0,0],
               [1,1,1,0,0,1,0]]
    print(best_match(match(people1)))
    # output is ([1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], 39.23)

    v0,v1 = (2,3,-1), (1,-3,5)
    print(angle(v0,v1)) #122

    v0,v1 = (3,4,-1),(2,-1,1)
    print(angle(v0,v1)) #85

    v0,v1 = (5,-1,1),(1,1,-1)
    print(angle(v0,v1)) #85


    # #problem 4
    l0 = (2,3)
    l1 = (-1/2,2)
    print(intersect(l0,l1)) #-2/5,11/5
    print(intersect((1,4),(-1/2,1/2)))
 
    #problem 5
    lst = [1,3,3,2,9,10]

    print(mean(lst))
    print(variance(lst))
    print(std(lst))
    print(mean_centered(lst))
    print(mean(mean_centered(lst)))

    #problem 6
    s = (-.025,-.5,60)
    d = (0.02,.6,20)
    print(equi(s,d))

