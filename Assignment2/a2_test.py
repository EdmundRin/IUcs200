import a2
import unittest

class MyTests(unittest.TestCase):

    def test_g(self):
        self.assertAlmostEqual(a2.g(1.01),3.01,2)
    def test_f(self):    
        self.assertAlmostEqual(a2.f(1988),17.6,2)
    def test_h0(self):    
        self.assertAlmostEqual(a2.h_0(0),110,2)  
    def test_h1(self):    
        self.assertAlmostEqual(a2.h_1(4),286,2)     
    def test_q(self):    
        self.assertAlmostEqual(a2.q((1,0,-1)),(1.0, -1.0))
    def test_eq(self):    
        self.assertAlmostEqual(a2.eq([20, "*", 19, 381]),False)   
    def test_path(self):    
        self.assertAlmostEqual(a2.path([1,0,1,0,0]),True)         
    def test_max3d(self):    
        self.assertAlmostEqual(a2.max3d(1,2,3),3)


if __name__=="__main__":
    unittest.main()
