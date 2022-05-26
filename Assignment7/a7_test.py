import a7
import unittest

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")


#### We have included basic test cases for most problems but not all
# You are encouraged to write some of your own cases for 
# example for Problems 1 and 2.

# This is done to encourage you think critically about the quality of your code
# and test where it can fail. For writing these test cases, you just need to 
# test the functions with new input arguments and expected output (that you already know).

# For example, for Problem1, if I want to check the multiplication of two fractions is
# returning the correct output or not then, I can call the relevent function with two fractions and 
# check the returned output against the expected value.

# f1 = Fraction(2, 3 )
# f2 = Fraction(3, 4)
# f3 = Fraction(1, 2)

# I know the correct answer for f1*f2 is (6, 12) --> reduced --> (1, 2) 
# I stored the correct answer in f3, and check this value against the output returned from the function
# self.assertEqual(f3, f1*f2)

# You can follow the same scheme for other functions like addition, equality
# and basically the same scheme for other problems as well.

class Testa7(unittest.TestCase):

    def test_Fraction(self):
        a = a7.Fraction(6,7)
        b = a7.Fraction(1,2)
        c = a7.Fraction(19,14)
        d = a7.Fraction(3,7)

        self.assertEqual(c, a + b)
        self.assertEqual(d, a * b)


    def test_cipher(self):
        sentence = "this is a secret message used for testing"
        shift = 4
        secret = a7.encrypt_sentence(sentence, shift)
        decode_secret = a7.decrypt_sentence(secret, shift)

        self.assertEquals(sentence, decode_secret)


    def test_TranslateDNA(self):
        pass


    def test_Function(self):
        pass




if __name__=="__main__":
    unittest.main()

