import math

#Problem 1

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    from math import exp
    return n_0 * exp (m*t)

#INPUT t days
#RETURN number of teeth
def N_t(t):
    from math import exp , ceil
    result = 71.8 * exp (-8.96*exp(-0.0685*t))
    return ceil (result)

#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    from math import log, ceil 
    R = 8.314
    T = 300
    W = R * T * log (P_i / P_f)
    return ceil(W)


#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    from math import ceil
    k = 0.0033
    L = k * (V**2) * A * C_l
    return ceil(L)

###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN True if discriminant is real, False otherwise
def q(t):
    a, b, c = t
    if b **2 - 4*a*c >= 0:
        return True
    else:
        return False


###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT item and list
#RETURN True if item is in the list
#CONSTRAINT You cannot use 'in' -- must use bounded looping
def m(x,lst):
    for i in lst:
        if i == x:
            return True
    return False 

def amt(r,no_tax):
    amt = 0
    for item in r:
        if not m(item[0],no_tax):
            item[1] *= 1.07
    # debug: print (r) 
    for item in r:
        amt += item[1]
    return round(amt,2)


###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT p0 = (x0,y0) p1 = (x1,y1)
#RETURN (a,b,c) for line ax + by + c = 0
def f(p0,p1):
    x1, y1 = p0
    x2, y2 = p1
    if x2 != x1:
        m = (y2 - y1)/(x2 - x1)
        b = y1 - m*x1 
        return (m,b)
    else:
        return ()




###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

err_msg = ["Data Error: 0 values", "Data Error: 0 in data"]

def arithmetic_mean(nlst):
    sum = 0
    for item in nlst:
        sum += item 
    return sum / len(nlst) 

def geo_mean(nlst):
    from math import log, exp 
    sum = 0
    for item in nlst:
        sum += log(item)
    return exp(sum/len(nlst))


def har_mean(nlst):
    sum = 0
    for item in nlst:
        sum += 1/item 
    return len(nlst) / sum 
    
def RMS_mean(nlst):
    from math import sqrt 
    sum = 0 
    for item in nlst:
        sum += item **2
    return sqrt (sum / len (nlst))

    

###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT x filters
#RETURN fixed cost
def F(x):
    fixed_c = 10000
    return fixed_c 

#INPUT x filters
#RETURN variable cost
def V(x):
    if 0 <= x <= 40000:
        var_c = -0.0001* x **2 + 10*x 
        return var_c

#INPUT x filters
#RETURN total cost
def C(x):
    total = F(x) + V(x)
    return total 

###########################################################################
# Functions for Problem 7
###########################################################################

#INPUT list [p,i,n] principal, interest rate, payments
#RETURN montly payment float
def Mortgage(house):
    p,i,n = house 
    m = p * (((i/1200)*((1+i/1200)**(n*12)) / (((1+i/1200)**(n*12)) - 1)))
    return round(m,2) 

#INPUT list [p,i,n] principal, interest rate, payments
#RETURN the difference between total payout and value
#of home 
#REQUIRES Mortgage function
def total_paid(house):
    p,i,n = house 
    total = Mortgage(house) * n * 12 - p 
    return round(total,2) 


###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT list of numbers
#RETURN True if geometric series, False otherwise
def is_geo(xlst):
    if len(xlst) <= 2:
        return 0
    else:
        for i in range(len(xlst)-2):
            if xlst[i+1]/xlst[i] != xlst[i+2] / xlst[i+1]:
                return 0
        return 1


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """
    # #problem 1
    print(N(500,100,4)) 
    print(N_t(1000))
    print(W(10,1))
    print(L(33.8,512,0.515))

    #problem 2
    print(q((1,4,-21)))
    print(q((3,6,10)))
    print(q((1,0,-4)))

    #problem 3
    receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
    no_tax = [33,5,2]
    print(amt(receipt,no_tax))

    # #problem 4
    print(f((2,3),(6,4)))
    print(f((1,6),(3,2)))
    print(f((1,3),(1,5)))
 
    #problem 5
    print(arithmetic_mean([1,2,3]))
    print(geo_mean([2,4,8]))
    print(har_mean([1,2,3]))
    print(RMS_mean([1,3,4,5,7]))

    #problem 6
    print(C(0))
    print(C(100))
    print(C(1000))

    #problem 7
    house = [300000,2.9,30]
    print(Mortgage(house))
    print(total_paid(house))

    # #problem 8
    xlst = [1/2,1/4,1/8,1/16,1/32]
    print(is_geo(xlst))
    xlst = [1,-3,9,-27]
    print(is_geo(xlst))
    xlst = [625,125,25]
    print(is_geo(xlst))
    xlst = [1/2,1/4,1/8,1/16,1/31]
    print(is_geo(xlst))
    xlst = [1,-3,9,-26]
    print(is_geo(xlst))
    xlst = [625,125,24]
    print(is_geo(xlst))
    print(is_geo([1/2,1/4]))