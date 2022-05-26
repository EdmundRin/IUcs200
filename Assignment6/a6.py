import math
import random as rn
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


########################
# PROBLEM 1
########################

# INPUT positive integers n and k
# RETURN an integer (result of n choose k as per equation 2 in HW PDF)
def C(n, k):
    # Create a helper func. to calculate the factorial:
    def helper(x):
        if x == 0:
            return 1
        else:
            return x * helper(x-1)
    # Calculate n choose k:
    if k == 0:
        return 1
    else:
        return int(helper(n)/(helper(k)*helper(n-k)))


# INPUT positive number m
# RETURN integer (the value of B(m) as per equation 4 in the PDF)
def B(m):
    if m == 0:
        return 1
    else:
        sum = 0
        for k in range(0,m):
            sum += C(m+1,k)*B(k)
        return -sum/(m+1)


########################
# PROBLEM 2
########################

# INPUT path and file name (read the file as per the format of Table-1 (in the PDF) and) retrn the list as per the output format given below
# RETURNS list of tuples [(0,1650), (10,1750),...,(110,6870)] 
# where each tuple correspond to a particular year (year, population in that year)
def get_data(path,name):
    with open(str(path+"/"+name), "r") as f:
        data = f.readlines()
    # Strip the contents of the file by line in order to remove the newline character
    data = [x.strip() for x in data]
    # debug:print(data)

    # Turn the contents of each line into a small list of strings
    data = [x.split(",") for x in data]
    # debug:print(data)

    # Split content by Tab
    data = [y.split(    ) for x in data for y in x]
    # debug:print(data)

    # Turn the contents of each string into an integer
    data = [(int(x[0]),int(x[1])) for x in data]
    # debug:print(data)

    # Create a list of tuples
    data = [tuple(x) for x in data]
    return data

# I don't know why this is part of assignment 7, I think it's a mistake in the title.
# So please allow me to change the path below to Assignment 6
data = get_data("Assignment6", "pop.txt")
# debug:print(data)

# INPUT year 0,10,20,...,110
# RETURN model population
# calculate the population it as per equation 16 in the PDF
def pop(year):
    return 1436.53*(1.01395**year)

# INPUT population data
# RETURN total error
# calculate total error as per equation 18 and 19
def error(data):
    error = 0
    for i in data:
        error += abs(i[1]-pop(i[0]))
    return error


########################
# PROBLEM 3
########################

# INPUT A string
# OUTPUT boolean (True or False)
def isogram(x):
    for char in x:
        if x.count(char) > 1:
            return False
    return True


########################
# PROBLEM 4
########################

# INPUT A string (in hexadecimal format)
# OUTPUT An intege{>L/""}
def Hex(n):
    order = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,\
            '9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    return sum([order[x]*(16**(len(n)-1-i)) for i,x in enumerate(n)])


########################
# PROBLEM 5
########################

# INPUT an integer
# OUTPUT boolean (True or False)
# return True if divisible by 11 otherwise False
def div_11(x):
    str_x = str(x)
    odd_sum = sum([int(str_x[i]) for i in range(0,len(str_x),2)])
    even_sum = sum([int(str_x[i]) for i in range(1,len(str_x),2)])
    if odd_sum-even_sum == 0:
        return True
    elif odd_sum-even_sum ==11:
        return True
    elif odd_sum-even_sum == -11:
        return True
    else:
        return False
    # Logic is only half correct.
    # For eg: 909095 is a number which is divisible by 11, yet your function outputs 'False' for this number.
    # You want to keep running your logic as long as the difference between the even_sum and odd_sum is more than 11.
    # In the current logic, you only run the logic once.


if __name__ == "__main__":
    # print("This is the code file. To see test results, please run 'a6_test.py'")
    # print("Feel free to write your own tests here. The tests you write below will not be graded.")

    ###### Problem 1
    print(C(1, 0)) # 1
    print(C(3, 1)) # 3
    print(C(4, 3)) # 4

    print(B(1)) # -0.5
    print(B(2)) # 0.16666666
    print(B(3)) # -0.0
    print(B(4)) # -0.033333333333333305


    ##### Problem 2
    ##### Code to plot the graph for error between true population and 
    # prediction from the model

    # Uncomment the below code to plot the graph for model prediction.
    # make sure to save the plot under the Assignment7 directory
    
    total_error = round(error(data),4)
    t = np.arange(0.0, 120.0)
    fig,ax = plt.subplots()

    ax.plot(t, pop(t),'g')
    for y,p in data:
        ax.plot(y,p,'ro--')

    ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    title = "Population Growth. Total ave error = %{0}".format(total_error))
    ax.grid()
    plt.show()

    
    ##### Problem 3
    print(isogram("hello")) # False
    print(isogram("hlo"))   # True
    print(isogram(""))      # True

    # Wrong format
    # ##### Problem 4
    # print(hex_dec(C1)) # 193

    # Problem 4
    print(Hex("C1")) # 193

    # Wrong format
    # ##### Problem 5
    # print(elevens(11)) # True
    # print(elevens(0))  # True
    # print(elevens(55)) # True

    # Problem 5
    print(div_11(11)) # True
    print(div_11(0))  # True
    print(div_11(55)) # True
