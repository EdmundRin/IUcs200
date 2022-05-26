########
########
# Write you code for midterm problems in this file.
# Do not change the name of this file.
########

#--------------problem 1----------------------
def f(xlst,n):
    result =  []
    for lst in xlst:
        if len(lst) > n:
            result += [lst]
    return result

#--------------problem 2----------------------
def gravity(m1,m2,d):
    g = 6.67*(10**(-11))
    if d != 0:
        f = (g*m1*m2)/(d**2)
    else:
        f = "error"
    return f

#--------------problem 3-----------------------
def tip_amt(t):
    # tip = {"bad":1.15,"good":1.2,"great":1.25}
    tip = {"bad":15,"good":20,"great":25}
    bill,comment = t
    # total = bill * tip[comment]
    total = bill * (1+0.01*tip[comment])
    return round(total,2)

#-----------------test-------------------------
if __name__ == "__main__":
    #--p1--
    x = [[1],[1,2],[1,2,3],[1,2,3,4]]
    print(f(x,1))
    print(f(x,2))
    print(f(x,3))
    print(f(x,-1))
    print(f(x,5))
    #--p2--
    m1,m2,d = 1,6e24,6.4e6
    print(gravity(m1,m2,d))
    #--p3--
    test = [(100,"great"), (40,"bad"),(50,"good")]
    for t in test:
        print(tip_amt(t))
