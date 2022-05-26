#input radius r, height h
#return volume

def c(r,h):
    from math import pi
    volume = (1/3)*pi*(r**2)*h
    return volume 

#input t days
#output oxygen conten percent of it normal level
def f(t):
    content = 100 * ( (t**2)+ 10*t + 100)/((t**2) + 20*t + 100)
    return content 


#input t hours
#return percent watching tv
def P(t):
    p = 0.01354*(t**4)-0.49375*(t**3)+2.58333*(t**2)+3.8*t+31.60704
    return p 

#input x percent
#return millions of dollars
def cost(x):
    c = (0.5*x)/(100 - x)
    return c 

#input dosage a mg and years t
#return child dosage mg
def D(t,a):
    dosage = a*(t+1)/24
    return dosage 


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here  """

    #volume of cone
    print("c(2,5)=",c(2,5)) 
    print("c(3,7)=",c(3,7))

    #oxygen content
    print("f(0)=",f(0))
    print("f(10)=",f(10))

    #tv watching
    print("P(0)=",P(0))
    print("P(3)=",P(3))
    print("P(8)=",P(8))

    #x% cost
    print("cost(50)=",cost(50))
    print("cost(70)=",cost(70))
    print("cost(90)=",cost(90))

    #cowling's rule
    print("D(4,500)=",D(4,500))
    print("D(5,500)=",D(4,500))