import a4
import unittest

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")


class TestA4(unittest.TestCase):

    def test_day(self):
        self.assertAlmostEqual(a4.day([14,2,2000]), "Mon")
        self.assertAlmostEqual(a4.day([14,2,1963]), "Thu")
        self.assertAlmostEqual(a4.day([14,2,1972]), "Mon")

    def test_q(self):
        self.assertAlmostEqual(a4.q((1,3,-4)), (-4.0, 1.0))
        self.assertAlmostEqual(a4.q((1,-2,-4)), (-1.24, 3.24))
        self.assertAlmostEqual(a4.q((1,-1,-4)), (-1.56, 2.56))

    
    def test_best_match(self):
        people = [[0,0,1],[1,0,0],[1,1,1]]
        people1 = [[0,1,1],[1,0,1],[1,1,1]]
        people2 = [[0,1,0],[1,0,1],[0,1,1]]
        self.assertEqual(a4.best_match(a4.match(people)), ([0, 0, 1], [1, 1, 1], 54.74))
        self.assertEqual(a4.best_match(a4.match(people1)), ([0, 1, 1], [1, 1, 1], 35.26))
        self.assertEqual(a4.best_match(a4.match(people2)), ([0, 1, 0], [0, 1, 1], 45.0))

    def test_intersect(self):
        self.assertEqual(a4.intersect((0,0), (2,2)), (-1.0, 0.0))
        self.assertEqual(a4.intersect((0,5), (4,2)), (0.75, 5.0))

    def test_mean(self):
        lst = [4,54,2,7,9,32,21,3,5,6,8]
        self.assertAlmostEqual(a4.mean(lst), 13.73)
        self.assertAlmostEqual(a4.variance(lst), 235.65)
        self.assertAlmostEqual(a4.std(lst), 15.35)
        self.assertAlmostEqual(a4.mean(a4.mean_centered(lst)), 0)

    def test_equi(self):
        self.assertEqual(a4.equi((-.025,-.5,60), (0.02,.6,20)), (20,-44.44))
        self.assertEqual(a4.equi((-.025,-5,60), (0.02,.6,20)), (6.77, -131.22))
        self.assertEqual(a4.equi((0.01, -3, 80), (0.2,6,30)), (5.02, -52.39))



if __name__=="__main__":
    unittest.main()

