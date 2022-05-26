import a5
import unittest
import random as rn

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")


class TestA5(unittest.TestCase):

    def test_entropy(self):
        self.assertAlmostEqual(a5.entropy([4, 5, 6, 2, 23, 43, 9]), 2.81)
        self.assertAlmostEqual(a5.entropy([23, 193, 23, 76, 0, 6, 12]), 2.52)
        self.assertAlmostEqual(a5.entropy([0, 1, 10, 100, 1000, 10000]), 2.58)
        self.assertAlmostEqual(a5.entropy([5, 6, 2, 1, 3]), 2.32)
        self.assertAlmostEqual(a5.entropy([0]), 0)

    def test_L(self):
        self.assertEqual(a5.L([1,0,0,1,1,0,1,0,1]), 2)
        self.assertEqual(a5.L([1,1,1,1,1,0,1,0,1]), 5)
        self.assertEqual(a5.L([1,0,0,7,1,5,1,4,1]), 1)

    def test_div_9(self):
        self.assertEqual(a5.div_9(0), True)
        self.assertEqual(a5.div_9(1), False)
        self.assertEqual(a5.div_9(100), False)
        self.assertEqual(a5.div_9(234209832), False)
        self.assertEqual(a5.div_9(123456789), True)

    def test_P(self):
        self.assertAlmostEqual(a5.p(5), 11040.808031999999)
        self.assertAlmostEqual(a5.p_t(5), 11040.808031999999)
        self.assertAlmostEqual(a5.p_t(5, 10), 11051.848840032)

    def test_C(self):
        self.assertAlmostEqual(a5.c(5), 66384)
        self.assertAlmostEqual(a5.c_t(4), 7048)
        self.assertAlmostEqual(a5.c_t(5, 10), 107344)

    def test_D(self):
        self.assertAlmostEqual(a5.d(5), 364)
        self.assertAlmostEqual(a5.d_t(5), 364)
        self.assertAlmostEqual(a5.d_t(5, 20), 4981)

    def test_potatoe(self):
        for _ in range(5):
            xlst = [rn.randint(1, 10) for i in range(10)]

            self.assertEqual(a5.potato(xlst), sorted(xlst))

    def test_msi(self):
        self.assertEqual(a5.msi([7, -9, 5, 10, -9, 6, 9, 3, 3, 9]), [2, 10, 36])

    def test_dollars(self):
        self.assertEqual(a5.dollars(2.24), [8, 2, 0, 4])
        self.assertEqual(a5.dollars(10.35), [41, 1, 0, 0])
        self.assertEqual(a5.dollars(1), [4, 0, 0, 0])
        self.assertEqual(a5.dollars(5), [20, 0, 0, 0])
        self.assertEqual(a5.dollars(0.41), [1, 1, 1, 1])





if __name__=="__main__":
    unittest.main()

