def even_number(lst):
    '''
    Given a list of integer as an input, return a new list contains all integers in lst that are even number.
    
    input:
    lst - a list of integer numbers

    output:
    a new list contains all of the even numbers in the input list. 
    '''
    
    newlist = []
    for item in lst:
        if item %2 == 0:
            newlist += [item,]
    return newlist 


def star_patern(n):
    '''
    given an integer n, write a function to print the bellow  
    note to do this operation you can't use the .append method for lists

    given n as an input, write a function that prints the bellow pattern:
    for example for n = 5:
    *
    **
    ***
    ****
    *****
    '''
    for i in range(1,n+1):
        print ("*"*i)


def print_num(n):
    '''
    given an input integer n, print numbers from n to 0 using while loops.

    for example for n = 5:
    5
    4
    3
    2
    1
    0

    input:
    n-integr number
    '''

    # for i in range (n,-1,-1):
        # print (i)
    while n >= 0:
        print(n)
        n -= 1


def dict_example(dict):
    '''
    we have a dict as an input that contains names of the candidate as a key 
    and the number of votes for that candidate as a value for that key. Please
    return the name of a peson who has the maximum votes.
    example:
    dict = {
        'john': 3,
        'mike': 32,
        'anna': 34,
        'leo': 16
    }

    expected ouput: 'anna'
    '''
    newlist = []
    namelist = []
    for item in dict.items():
        newlist += [item[1]]
    for item in dict.items():
        if item[1] == max(newlist):
            # return item[0]
            # -This return is the situation where I did not consider flat tickets before
            namelist += [item[0]]
    # I want to try to make it return if there is a tie vote
    if len(namelist) == 1:
        return namelist [0]
    else:
        return namelist
        # but the type of it is list
        # the problem needs a return instead of print something
        # so I dont know hot to return like mutiple values

if __name__ == '__main__':
    # TODO:
    # implement testing
    print(even_number([3, 6, 2, 99, 32]))

    star_patern(5)

    print_num(5)

    dict = {
        'john': 3,
        'mike': 32,
        'anna': 34,
        'leo': 16 }
    print(dict_example(dict))
