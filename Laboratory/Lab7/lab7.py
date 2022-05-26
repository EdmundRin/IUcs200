###########################################################
# factorial
###########################################################

def factorial(n):
    """
    Recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1) 

def tail_factorial(n, a=1):
    """
    Tail-recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n == 0:
        return a 
    else:
        return tail_factorial(n-1,n*a)  

d = {}
def memo_factorial(n):
    """
    Memoized function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n not in d.keys():
        if n <=1:
            d[n] = 1
        else:
            d[n] = n*memo_factorial(n-1)
    return d[n] 

###########################################################
# only_ints
###########################################################

def only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if not xlist:
        return []
    elif isinstance(xlist[0],int):
        return [xlist[0]] + only_ints(xlist[1:])
    else:
        return only_ints(xlist[1:])



def tail_only_ints(xlist, a=[]):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if not xlist:
        return a
    elif isinstance(xlist[0],int):
        return tail_only_ints(xlist[1:],a +[xlist[0]])
    else:
        return tail_only_ints(xlist[1:],a) 
        

d = {}
def memo_only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if "x" not in d.keys():
        if not xlist:
            return []
        elif isinstance(xlist[0],int):
            d["x"] = [xlist[0]] + memo_only_ints(xlist[1:])
        else:
            d["x"] = memo_only_ints(xlist[1:])
    return d["x"] 



if __name__ == "__main__":
    # Write your own print statements here
    # to briefly test your code

    # only int test:
    x = [1,2,3,"a"]
    y = ["a",2,3,4]
    z = [1,2,"a",4]
    print(only_ints(x))
    print(only_ints(y))
    print(only_ints(z)) 
    
    # tail only int test:
    x = [1,2,3,"a"]
    y = ["a",2,3,4]
    z = [1,2,"a",4]
    print(tail_only_ints(x))
    print(tail_only_ints(y))
    print(tail_only_ints(z))

    # memo only int test:
    x = [1,2,3,"a"]
    y = ["a",2,3,4]
    z = [1,2,"a",4]
    print(memo_only_ints(x))
    print(memo_only_ints(y))
    print(memo_only_ints(z))