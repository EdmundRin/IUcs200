# Assignment 7

- Username: cl101
- Commit hash used for grading: 726f4b5dcbb45f7d133046874329b54bf3bc6bad

- Graded by: Tim Chan

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 85.7/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (39.7/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `Fraction`:4.0/11
    - TA Comments: 
    - In this case all you needed was to assign the parameters to their respective variables. Like self.numerator = numerator etc. You shouldn't need to import gcd. Gcd is actually something you code yourself. 
    - get was simply returning the numerator and denominator. It helps you use it in later sections. So return self.numerator, self.denominator would be fine
    - Denominator is white in __add__ on line 39, meaning that the program doesn't really know what it is. That is where the get(self) comes in. Because that returns the numerator and denominator. So you can have other.get() and it will grab that information which you can use by indexing.


- Problem 2:
    - `encrypt`: 1.7/2
    - `decrypt`: 2.0/2
    - `encryptsentence`: 3.0/5
    - `decryptsentence`: 3.0/4
    - TA Comments: 
    - Issue with encrypt was that there is sometime an annoyting case when someone wants to shift more than 27 spaces. When that happens, you can't just subtract or add 27 to shift it back. Modulus is a better choice because it returns the remainder. So 7%2 = 1, because 2*3 is 6 and 7-6 = 1. The remainder is 1. 
    - Same issue with decrypt
    - lost pts on encrypt sentence and decrypt because of the above issues


- Problem 3:
    - `getaminoacids`: 5.0/5
    - `getDNA`: 5.0/5
    - `translate`: 3.0/3
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `Function`:13.0/13
    - TA Comments: TA did not add any comments.



## Code Review & style (46/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.


- Problem 1:
    - `Fraction`:7/11
    - TA Comments: Logic makes sense in most parts.


- Problem 2:
    - `encrypt`: 2/2
    - `decrypt`: 2/2
    - `encryptsentence`: 5/5
    - `decryptsentence`: 4/4
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `getaminoacids`: 5/5
    - `getDNA`: 5/5
    - `translate`: 3/3
    - TA Comments: Good job!


- Problem 4:
    - `Function`:13/13
    - TA Comments: TA did not add any comments.


## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_Fraction_5_basic
ERROR: Test case for function: Fraction_eq_repr
ERROR: Input: (5, 7)
ERROR: Actual output: Frac(5/7)
ERROR: Expected output: frac(5/7)
ERROR: 'frac(5/7)' != 'Frac(5/7)'
- frac(5/7)
? ^
+ Frac(5/7)
? ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'frac(5/7)' != 'Frac(5/7)'
- frac(5/7)
? ^
+ Frac(5/7)
? ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 219, in test_a_Fraction_5_basic
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'frac(5/7)' != 'Frac(5/7)'
- frac(5/7)
? ^
+ Frac(5/7)
? ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_Fraction_5_basic
ERROR: Test case for function: Fraction_eq_repr
ERROR: Input: (1, 2)
ERROR: Actual output: Frac(1/2)
ERROR: Expected output: frac(1/2)
ERROR: 'frac(1/2)' != 'Frac(1/2)'
- frac(1/2)
? ^
+ Frac(1/2)
? ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'frac(1/2)' != 'Frac(1/2)'
- frac(1/2)
? ^
+ Frac(1/2)
? ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 219, in test_a_Fraction_5_basic
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'frac(1/2)' != 'Frac(1/2)'
- frac(1/2)
? ^
+ Frac(1/2)
? ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_Fraction_5_basic
ERROR: Test case for function: Fraction_eq_repr
ERROR: Input: (4, 5)
ERROR: Actual output: Frac(4/5)
ERROR: Expected output: frac(4/5)
ERROR: 'frac(4/5)' != 'Frac(4/5)'
- frac(4/5)
? ^
+ Frac(4/5)
? ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'frac(4/5)' != 'Frac(4/5)'
- frac(4/5)
? ^
+ Frac(4/5)
? ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 219, in test_a_Fraction_5_basic
    self.assertEqual(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'frac(4/5)' != 'Frac(4/5)'
- frac(4/5)
? ^
+ Frac(4/5)
? ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((1, 2), (4, 5))
ERROR: Actual output: Frac(1,3/10)
ERROR: Expected output: ((13, 10), 'frac(1,3/10)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 309, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((6, 7), (1, 2))
ERROR: Actual output: Frac(1,5/14)
ERROR: Expected output: ((19, 14), 'frac(1,5/14)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 309, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((2, 4), (4, 8))
ERROR: Actual output: Frac(1,0/1)
ERROR: Expected output: ((4, 4), 'frac(1,0/1)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 309, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((27, 9), (12, 3))
ERROR: Actual output: Frac(7,0/1)
ERROR: Expected output: ((7, 1), 'frac(7,0/1)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 309, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((1, 2), (4, 1))
ERROR: Actual output: Frac(2,0/1)
ERROR: Expected output: ((4, 2), 'frac(2,0/1)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 330, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((6, 7), (1, 2))
ERROR: Actual output: Frac(3/7)
ERROR: Expected output: ((3, 7), 'frac(3/7)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 330, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((7, 3), (5, 2))
ERROR: Actual output: Frac(5,5/6)
ERROR: Expected output: ((35, 6), 'frac(5,5/6)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 330, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_Fraction_2_hard
ERROR: Test case for function: Fraction_all
ERROR: Input: ((4, 3), (1, 2))
ERROR: Actual output: Frac(2/3)
ERROR: Expected output: ((2, 3), 'frac(2/3)')
ERROR: False is not true
ERROR: ----------------------------------------------------------------------------
ERROR: False is not true
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 330, in test_c_Fraction_2_hard
    self.assertTrue(actual_output.__repr__() == expected_output[1])
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 680, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_d_encrypt_2
ERROR: Test case for function: encrypt
ERROR: Input: ('z', 1) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: `
ERROR: Expected output: {
ERROR: '{' != '`'
- {
+ `

ERROR: ----------------------------------------------------------------------------
ERROR: '{' != '`'
- {
+ `
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: '{' != '`'
- {
+ `

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_encryptsentence_5
ERROR: Test case for function: encrypt_sentence
ERROR: Input: ('this is a secret message used for testing', 0) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: this`is`a`secret`message`used`for`testing
ERROR: Expected output: this{is{a{secret{message{used{for{testing
ERROR: 'this{is{a{secret{message{used{for{testing' != 'this`is`a`secret`message`used`for`testing'
- this{is{a{secret{message{used{for{testing
?     ^  ^ ^      ^       ^    ^   ^
+ this`is`a`secret`message`used`for`testing
?     ^  ^ ^      ^       ^    ^   ^

ERROR: ----------------------------------------------------------------------------
ERROR: 'this{is{a{secret{message{used{for{testing' != 'this`is`a`secret`message`used`for`testing'
- this{is{a{secret{message{used{for{testing
?     ^  ^ ^      ^       ^    ^   ^
+ this`is`a`secret`message`used`for`testing
?     ^  ^ ^      ^       ^    ^   ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'this{is{a{secret{message{used{for{testing' != 'this`is`a`secret`message`used`for`testing'
- this{is{a{secret{message{used{for{testing
?     ^  ^ ^      ^       ^    ^   ^
+ this`is`a`secret`message`used`for`testing
?     ^  ^ ^      ^       ^    ^   ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_f_encryptsentence_5
ERROR: Test case for function: encrypt_sentence
ERROR: Input: ('aaaaa zzzzzzzz', 81) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: ±°°°°°°°°
ERROR: Expected output: aaaaa{zzzzzzzz
ERROR: 'aaaaa{zzzzzzzz' != '\x97\x97\x97\x97\x97±°°°°°°°°'
- aaaaa{zzzzzzzz
+ ±°°°°°°°°

ERROR: ----------------------------------------------------------------------------
ERROR: 'aaaaa{zzzzzzzz' != '\x97\x97\x97\x97\x97±°°°°°°°°'
- aaaaa{zzzzzzzz
+ ±°°°°°°°°
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'aaaaa{zzzzzzzz' != '\x97\x97\x97\x97\x97±°°°°°°°°'
- aaaaa{zzzzzzzz
+ ±°°°°°°°°

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_g_decryptsentence_4
ERROR: Test case for function: decrypt_sentence
ERROR: Input: ('aaaaa{zzzzzzzz', 81) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: +++++EDDDDDDDD
ERROR: Expected output: aaaaa zzzzzzzz
ERROR: 'aaaaa zzzzzzzz' != '+++++EDDDDDDDD'
- aaaaa zzzzzzzz
+ +++++EDDDDDDDD

ERROR: ----------------------------------------------------------------------------
ERROR: 'aaaaa zzzzzzzz' != '+++++EDDDDDDDD'
- aaaaa zzzzzzzz
+ +++++EDDDDDDDD
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment7/cl101/Assignment7/a7_hidden_test.py", line 187, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: 'aaaaa zzzzzzzz' != '+++++EDDDDDDDD'
- aaaaa zzzzzzzz
+ +++++EDDDDDDDD

ERROR: ============================================================================
```
```
