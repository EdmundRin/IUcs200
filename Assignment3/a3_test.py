import a3
import unittest
import random as rn

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")


class TestA3(unittest.TestCase):

    def test_N(self):
        self.assertAlmostEqual(a3.N(500,100,4)/(1e176),2.61,1) 
        self.assertAlmostEqual(a3.N(250,30,2)/(1e28),2.86,1) 
        self.assertAlmostEqual(a3.N(100,14,1)/(1e8),1.20,1) 

    def test_N_t(self):
        self.assertEqual(a3.N_t(1000),72) 
        self.assertEqual(a3.N_t(75),69) 
        self.assertEqual(a3.N_t(50),54) 
    def test_W(self):
        self.assertEqual(a3.W(10,1),5744) 
        self.assertEqual(a3.W(10,2),4015) 
        self.assertEqual(a3.W(20,1.5),6461) 

    def test_L(self):
        self.assertEqual(a3.L(33.8,512,0.515),995) 
        self.assertEqual(a3.L(30.8,512,0.515),826) 
        self.assertEqual(a3.L(25.8,512,0.515),580) 

    def test_q(self):
        self.assertTrue(a3.q((1,4,-21))) 
        self.assertFalse(a3.q((3,6,10)))
        self.assertTrue(a3.q((1,0,-4)))
         
    def test_amt(self):
        r = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
        no_tax = [33,5,2]
        self.assertAlmostEqual(a3.amt(r,no_tax),15.7,2) 

    def test_f(self):
        self.assertEqual(a3.f((2,3),(6,4)),(0.25,2.5))
        self.assertEqual(a3.f((1,6),(3,2)),(-2.0,8.0))
        self.assertEqual(a3.f((1,3),(1,5)),())
        
    def test_stats(self):
        er_msg0 = "Data Error: 0 values"
        er_msg1 = "Data Error: 0 in data"
        vlst = [[[], er_msg0], [[34,24.3],29.15], \
        [[2500, 2700, 2400, 2300, 2550, 2650, 2750, 2450, 2600, 2400],2530.0]]
        for i,j in vlst:
            if isinstance(j,str):
                self.assertEqual(a3.arithmetic_mean(i), j)
            else:
                self.assertAlmostEqual(a3.arithmetic_mean(i),j,2)
        self.assertEqual(a3.geo_mean([]), er_msg0)
        self.assertAlmostEqual(a3.geo_mean([3,5,6,6,7,10,12]),6.43,2)
        self.assertEqual(a3.har_mean([1,2.3,0,5]), er_msg1)
        self.assertEqual(a3.har_mean([]), er_msg0)
        self.assertAlmostEqual(a3.har_mean([2,4,8]),3.43,2)
        self.assertAlmostEqual(a3.har_mean([3,5,6,6,7,10,12]),5.87,2)
        self.assertEqual(a3.RMS_mean([]), er_msg0)
        self.assertAlmostEqual(a3.RMS_mean([3,5,6,6,7,10,12]),7.55,2) 


    def test_C(self):
        self.assertEqual(a3.C(0),10000.0)
        self.assertEqual(a3.C(100),10999.0)
        self.assertEqual(a3.C(1000),19900.0)
        
    def test_realestate(self):
        house1 = [[300000,2.9,30],1248.69, 149528.4]
        house2 = [[100000,6.0,30],599.55,115838.0]
        self.assertAlmostEqual(a3.Mortgage(house1[0]),house1[1],2)
        self.assertAlmostEqual(a3.total_paid(house1[0]), house1[2],2)
        self.assertAlmostEqual(a3.Mortgage(house2[0]),house2[1],2)
        self.assertAlmostEqual(a3.total_paid(house2[0]), house2[2],2)

if __name__=="__main__":
    unittest.main()

