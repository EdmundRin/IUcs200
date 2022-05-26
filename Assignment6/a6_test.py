import a6 as a6
import unittest
import random as rn

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")


#### We have included basic test cases for most problems but not all
# You are encouraged to write some of your own cases for 
# example for Problem-2.


class TestA6(unittest.TestCase):

    def test_C(self):
        self.assertEqual(a6.C(1, 0), 1)
        self.assertEqual(a6.C(3, 1), 3)
        self.assertEqual(a6.C(4, 3), 4)
        self.assertEqual(a6.C(3, 2), 3)
        self.assertEqual(a6.C(4, 2), 6)


    def test_B(self):
        self.assertAlmostEqual(a6.B(0), 1.0)
        self.assertAlmostEqual(a6.B(1), -0.5)
        self.assertAlmostEqual(a6.B(3), -0.0)
        self.assertAlmostEqual(a6.B(4), -0.033333333333)


    def test_is_isogram(self):
        self.assertEqual(a6.isogram(''), True)
        self.assertEqual(a6.isogram('HeHlo'), False)
        self.assertEqual(a6.isogram('This_is_good'), False)
        self.assertEqual(a6.isogram('Not'), True)
        self.assertEqual(a6.isogram('!Nay'), True)


    def test_Hex(self):
        self.assertEqual(a6.Hex('C1'), 193)
        self.assertEqual(a6.Hex('CB78'), 52088)
        self.assertEqual(a6.Hex('C78'), 3192)
        self.assertEqual(a6.Hex('B43'), 2883)


    def test_div_11(self):
        self.assertEqual(a6.div_11(11), True)
        self.assertEqual(a6.div_11(0), True)
        self.assertEqual(a6.div_11(33), True)
        self.assertEqual(a6.div_11(120), False)


if __name__=="__main__":
    unittest.main()

