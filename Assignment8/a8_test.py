import a8
import unittest

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")


#### We have included basic test cases for most problems but not all
# You are encouraged to write your own cases to test your code.

# This is done to encourage you think critically about the quality of your code
# and test where it can fail. For writing these test cases, you just need to 
# test the functions with new input arguments and expected output (that you already know).

# If you don't know how to write the test cases: We also gave a detailed 
# example of how to do this in the test file for Assignment7. Starting from there may help.

class TestA8(unittest.TestCase):

    def test_distance(self):
      point1 = (0,0)
      point2 = (5,3)
      point3 = (1,8)
      point4 = (2,4)
      self.assertEqual(a8.distance(point1, point1), 0)
      self.assertEqual(a8.distance(point3, point4), 4.123105625617661)
      self.assertEqual(a8.distance(point2, point4), 3.1622776601683795)
      self.assertEqual(a8.brute([point1, point2, point3, point4]), [point2, point4, 3.1622776601683795])


    def test_productivity(self):
      self.assertEqual(a8.productivity(10), 218.20000000000005)
      self.assertEqual(a8.productivity(11), 239.58000000000004)



    def test_permutation(self):
      result = [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2],
                  [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3],
                  [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
                  [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1],
                  [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2],
                  [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
      self.assertEqual(a8.permutation([1,2,3,4]), result)






if __name__=="__main__":
    unittest.main()

