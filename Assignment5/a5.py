import math
import random as rn


########################
# PROBLEM 1
########################

#INPUT positive number n
#RETURN log of number base 2
def log_2(n):
    from math import log2
    if n != 0:
        return log2(n)
    else:
        return 0

#INPUT list of immutable objects
#RETURN list of probability distribution
def makeProbability(xlst):
    dict1 = {}
    total = 0
    plst = []
    for i in xlst:
        total += 1
        if i not in dict1.keys():
            dict1[i] = 1
        else:
            dict1[i] += 1
    for v in dict1.values():
        plst += [v/total]
    return plst


#INPUT probability distribution
#RETURN non-negative number entropy
# You CANNOT use count()
def entropy(xlst):
    # Step 1: Get the probability of each element
    # Step 2: Get summation of entropy function
    # Step 3: Round summation to 2 decimal places
    plst = makeProbability(xlst)
    result = 0
    while plst:
        result += plst[0]*log_2(plst[0])
        plst = plst[1:]
    return round(-1*result,2)



########################
# PROBLEM 2
########################

#INPUT list of 0s 1s
#OUTPUT longest list of 1s
def L(x):
    str1 = ""
    for i in x:
        str1 += str(i)
    newlist = str1.split("0")
    # for i in max(newlist):
        # if i != "1":
            # newlist.remove(max(newlist))
    def helper(xlist):       # Used to exclude malicious input
        for i in max(xlist):
            if i !="1":
                xlist.remove(max(xlist))
            else:
                return max(xlist)
        return helper(xlist)
    return len(helper(newlist))


########################
# PROBLEM 3
########################

#INPUT non-negative integer
#OUTPUT True if divisible by 9, False otherwise
# You CANNOT use modulus (%) AND you CANNOT directly divide by 9
def div_9(x):
    if x == 0:
        return True
    total = 0
    t_str =  str(x)
    for i in t_str:
        total += int(i)
    total = str(total)
    if len(total) != 1:
        return div_9(total)
    elif total == "9":
        return True
    else:
        return False


########################
# PROBLEM 4
########################

#INPUT set of recurrence equations
#OUTPUT implement recursively, tail recursive generator
def p(n):
    if n == 0:
        return 10000
    else:
        return p(n-1)+0.02*p(n-1)

def p_t(n,v=0):
    pass

def p_g():
    n = 10000
    while True:
        yield n
        n = n + 0.02*n



def c(n):
    if n == 1:
        return 9
    else:
        return 9*c(n-1) + 10**(n-1) - c(n-1)

def c_t(n,v=0):
    pass

def c_g():
    n = 1
    while True:
        yield c(n)
        n += 1




def d(n):
    if n == 0:
        return 1
    else:
        return 3*d(n-1)+1

def d_t(n,v=1):
    pass

def d_g():
    n = 1
    while True:
        yield n
        n = 3*n +1




########################
# PROBLEM 5
########################

#INPUT list of numbers
#OUTPUT list sorted ascending using potato-smith

#INPUT list of numbers
#OUTPUT return sorted ascending
def insertion(a):
    for firstUI in range(len(a)):
        i = firstUI
        while i > 0:
            if a[i] < a [i-1]:
                a[i],a[i-1] = a[i-1],a[i]
                i -= 1
            else:
                break
    return a

#INPUT list of numbers
#OUTPUT sorted list ascending using potato and insertion
def potato(x): # error
    if len(x)<2:
        return x
    s = 2
    while s < len(x):
        if s < 2:
            for i in range(0,len(x)-1,s):
                if x[i] > x[i+1]:
                    x[i],x[i+1] = x[i+1],x[i]
        else:
            for i in range(s,len(x),s):
                if x[i-s:int(i/2)] > x[int(i/2):i]:
                    x[i-s:int(i/2)],x[int(i/2):i] = x[int(i/2):i],x[i-s:int(i/2)]
        s *= 2
    return x


########################
# PROBLEM 6
########################

#INPUT list of numbers
#OUTPUT  [a,b,c] where:
#    a = start index
#    b = end index
#    c = maximal sum of these indices
# You may use sum(list)
# Be cautious to use sum correctly - don't use it as a variable. It's a built-in function name.
def msi(x):
    n = len(x)
    maxi = 0
    start = 0
    end = 0
    x_sum = 0
    for i in range(n):
        x_sum = 0
        for j in range(i,n):
            x_sum += x[j]
            if x_sum > maxi:
                maxi = x_sum
                start = i
                end = j + 1
    return [start,end,maxi]



########################
# PROBLEM 7
########################

#INPUT positive number w/ two decimal places
#OUTPUT [q,d,n,p] which is the minimal amount of coins needed
def dollars(x):
    x *= 100
    q = int(x//25)
    d = int(x%25//10)
    n = int(x%25%10//5)
    p = int(x%25%10%5//1)
    return [q,d,n,p]





if __name__ == "__main__":
#     # Feel free to add your own tests here to help with error handling. 
#     print("This is the code file. To see test results, please run 'test_a5.py'")
#     print("Feel free to write your own tests here. The tests you write below will not be graded.")

    # #Problem 1
    s0 = ["a", "b", "a", "c", "c", "a"]
    print(entropy(s0))
 
    # #Problem  2
    x = [0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(L(x))

    # #Problem 3
    xlst = [99,0,18273645,22,27]
    for i in xlst:
        print(div_9(i))

    # Problem 4
    # for i,j in zip(range(10),p_g()):
    #     print(i,p(i),p_t(i),j)
    '''
    0 10000 10000 10000
    1 10200.0 10200.0 10200.0
    2 10404.0 10404.0 10404.0
    3 10612.08 10612.08 10612.08
    4 10824.3216 10824.3216 10824.3216
    5 11040.808031999999 11040.808031999999 11040.808031999999
    6 11261.62419264 11261.62419264 11261.62419264
    7 11486.8566764928 11486.8566764928 11486.8566764928
    8 11716.593810022656 11716.593810022656 11716.593810022656
    9 11950.925686223109 11950.925686223109 11950.925686223109
    '''
    # for i,j in zip(range(1,10),c_g()):
    #     print(i,c(i),c_t(i),j)
    '''
    1 9 9 9
    2 82 82 82
    3 756 756 756
    4 7048 7048 7048
    5 66384 66384 66384      
    6 631072 631072 631072   
    7 6048576 6048576 6048576
    8 58388608 58388608 58388608
    9 567108864 567108864 567108864
    '''
    # for i,j in zip(range(10),d_g()):
    #     print(i,d(i),d_t(i),j)
    '''
    0 1 1 1
    1 4 4 4
    2 13 13 13      
    3 40 40 40      
    4 121 121 121   
    5 364 364 364   
    6 1093 1093 1093
    7 3280 3280 3280
    8 9841 9841 9841
    9 29524 29524 29524
    '''
    #Problem 5
    lst = [rn.randint(0,100) for _ in range(rn.randint(1,20))]

    print(lst)
    print(potato(lst))
    
    
    #Problem 6

    x = [7, -9, 5, 10, -9, 6, 9, 3, 3, 9]
    data = [(-1)**rn.randint(0,1)*rn.randint(1,10) for _ in range(10)]
    print(msi(x))
    print(data)
    print(msi(data))

    #Problem 7
    xlt = [2.24,1.19,4.16,1.01,1.10,2.00]
    for i in xlt:
        print(dollars(i))
