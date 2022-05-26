# Put all your code for the Final exam in this file
# Make sure that you test your code before submission.

# Due to time constraints, there won't be grade review for the coding portion of the 
# exam so ensure that your submission is correct and run without errors.

# This file is left empty intentionally, you can use the code from the PDF as a starting point.

import numpy as np

#--------------------------class definition begins------------------------------
class Triangle:

    def __init__(self, p=[]):
        self.__p = np.array(p)
    
    # add for get p
    def get_p(self):
        return self.__p
    # add for reset p
    def reset_p(self, p=[]):
        self.__p = np.array(p)

    def area_d(self):
        d_ = []
        for i in range(3):
            d_.append([i for i in self.__p[i]]+[1])
        return round (abs(np.linalg.det(np.array(d_)))/2, 2)
    
    def distance(self,p0,p1):
        x0,y0 =  self.__p[p0]
        x1,y1 =  self.__p[p1]
        return ((x0-x1)**2 + (y0-y1)**2)**(1/2)

    # def the herron() function calculates the area of the triangle.
    #     Differently from the linear algebra approach used in area_d().
    #     For a triangle that has lengths a, b, c:
    #     s = (a + b + c) / 2
    #     area = sqrt(s(s-a)(s-b)(s-c))
    def herron(self):
        a,b,c = self.distance(0,1), self.distance(1,2), self.distance(2,0)
        s = (a+b+c)/2
        return round (np.sqrt(s*(s-a)*(s-b)*(s-c)), 2)
    
    def __eq__(self, other):
        return self.herron() == other.herron()
    
    # Some extra content:
    
    # def area_s(self):
        # return round (np.sqrt(np.dot(np.cross(self.__p[1]-self.__p[0], self.__p[2]-self.__p[0]), np.cross(self.__p[1]-self.__p[0], self.__p[2]-self.__p[0])))/2, 2)
    
    # def area_p(self):
        # return round (np.linalg.norm(np.cross(self.__p[1]-self.__p[0], self.__p[2]-self.__p[0]))/2, 2)

#-------------------------class definition ends----------------------------------



#-------------------------program begins here------------------------------------
t = Triangle([[-2,2], [1,5], [6,1]])
s = Triangle([[4,4], [2,-2], [-4,0]])
r = Triangle([[-1,1],[2,6],[7,1]])

print(t.area_d())
print(r.area_d())
print(s.area_d())
print(t.herron())
print(r.herron())
print(s.herron())

print(t == r)
print(r == s)
print(t == s)

print("----------------------------------------------------")
x = Triangle([[0,0],[3,0],[3,4]])
y = Triangle([[0,0],[4,0],[4,3]])
print (x.area_d())
print (y.area_d())
# print (x.area_s())
# print (y.area_s())
# print (x.area_p())
# print (y.area_p())
print (x.herron())
print (y.herron())
print(x == y)