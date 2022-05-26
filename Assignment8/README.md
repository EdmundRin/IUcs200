# Assignment 8

- Username: cl101
- Commit hash used for grading: 7334143072875858ccfc0ba6957f47a01f47ae5c

- Graded by: Jacob Fritz

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 93.6/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (43.6/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `step`:3.6/10
    - TA Comments: You did not implement the step properly. Check the pdf closely 


- Problem 2:
    - `distance`: 5.0/5
    - `brute`: 5.0/5
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `productivity`: 10.0/10
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `permutation`:10.0/10
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `Vector`:10/10
    - TA Comments: Your Str representation was missing some spaces, I added those points back for you



## Code Review & style (50/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.


- Problem 1:
    - `step`:10/10
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `distance`: 5/5
    - `brute`: 5/5
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `productivity`: 10/10
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `permutation`:10/10
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `Vector`:10/10
    - TA Comments: TA did not add any comments.


## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 2 direction: 2
ERROR: Actual output: (-1.0, 0.0)
ERROR: Expected output: (0, 0)
ERROR: Tuples differ: (0, 0) != (-1.0, 0.0)

First differing element 0:
0
-1.0

- (0, 0)
+ (-1.0, 0.0)
ERROR: ----------------------------------------------------------------------------
ERROR: Tuples differ: (0, 0) != (-1.0, 0.0)

First differing element 0:
0
-1.0

- (0, 0)
+ (-1.0, 0.0)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 129, in test_a_step_10
    self.assertEqual(expected_output[index], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1046, in assertTupleEqual
    self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Tuples differ: (0, 0) != (-1.0, 0.0)

First differing element 0:
0
-1.0

- (0, 0)
+ (-1.0, 0.0)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 4 direction: 4
ERROR: Actual output: (0.0, -1.0)
ERROR: Expected output: (0, 0)
ERROR: Tuples differ: (0, 0) != (0.0, -1.0)

First differing element 1:
0
-1.0

- (0, 0)
+ (0.0, -1.0)
ERROR: ----------------------------------------------------------------------------
ERROR: Tuples differ: (0, 0) != (0.0, -1.0)

First differing element 1:
0
-1.0

- (0, 0)
+ (0.0, -1.0)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 129, in test_a_step_10
    self.assertEqual(expected_output[index], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1046, in assertTupleEqual
    self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Tuples differ: (0, 0) != (0.0, -1.0)

First differing element 1:
0
-1.0

- (0, 0)
+ (0.0, -1.0)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 1
ERROR: Actual output: (2.0, 0.0)
ERROR: Expected output: (1, 0)
ERROR: Tuples differ: (1, 0) != (2.0, 0.0)

First differing element 0:
1
2.0

- (1, 0)
+ (2.0, 0.0)
ERROR: ----------------------------------------------------------------------------
ERROR: Tuples differ: (1, 0) != (2.0, 0.0)

First differing element 0:
1
2.0

- (1, 0)
+ (2.0, 0.0)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 129, in test_a_step_10
    self.assertEqual(expected_output[index], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1046, in assertTupleEqual
    self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Tuples differ: (1, 0) != (2.0, 0.0)

First differing element 0:
1
2.0

- (1, 0)
+ (2.0, 0.0)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 1
ERROR: Actual output: (3.0, 0.0)
ERROR: Expected output: (1, 0)
ERROR: Tuples differ: (1, 0) != (3.0, 0.0)

First differing element 0:
1
3.0

- (1, 0)
+ (3.0, 0.0)
ERROR: ----------------------------------------------------------------------------
ERROR: Tuples differ: (1, 0) != (3.0, 0.0)

First differing element 0:
1
3.0

- (1, 0)
+ (3.0, 0.0)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 129, in test_a_step_10
    self.assertEqual(expected_output[index], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1046, in assertTupleEqual
    self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Tuples differ: (1, 0) != (3.0, 0.0)

First differing element 0:
1
3.0

- (1, 0)
+ (3.0, 0.0)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 2
ERROR: Actual output: (2.0, 0.0)
ERROR: Expected output: (-1, 0)
ERROR: Tuples differ: (-1, 0) != (2.0, 0.0)

First differing element 0:
-1
2.0

- (-1, 0)
+ (2.0, 0.0)
ERROR: ----------------------------------------------------------------------------
ERROR: Tuples differ: (-1, 0) != (2.0, 0.0)

First differing element 0:
-1
2.0

- (-1, 0)
+ (2.0, 0.0)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 129, in test_a_step_10
    self.assertEqual(expected_output[index], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1046, in assertTupleEqual
    self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Tuples differ: (-1, 0) != (2.0, 0.0)

First differing element 0:
-1
2.0

- (-1, 0)
+ (2.0, 0.0)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 3
ERROR: Actual output: (2.0, 1.0)
ERROR: Expected output: (0, 1)
ERROR: Tuples differ: (0, 1) != (2.0, 1.0)

First differing element 0:
0
2.0

- (0, 1)
+ (2.0, 1.0)
?  ++    ++

ERROR: ----------------------------------------------------------------------------
ERROR: Tuples differ: (0, 1) != (2.0, 1.0)

First differing element 0:
0
2.0

- (0, 1)
+ (2.0, 1.0)
?  ++    ++
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 129, in test_a_step_10
    self.assertEqual(expected_output[index], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1046, in assertTupleEqual
    self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Tuples differ: (0, 1) != (2.0, 1.0)

First differing element 0:
0
2.0

- (0, 1)
+ (2.0, 1.0)
?  ++    ++

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_a_step_10
ERROR: Test case for function: step
ERROR: Input: i: 1 direction: 4
ERROR: Actual output: (2.0, 0.0)
ERROR: Expected output: (0, -1)
ERROR: Tuples differ: (0, -1) != (2.0, 0.0)

First differing element 0:
0
2.0

- (0, -1)
+ (2.0, 0.0)
ERROR: ----------------------------------------------------------------------------
ERROR: Tuples differ: (0, -1) != (2.0, 0.0)

First differing element 0:
0
2.0

- (0, -1)
+ (2.0, 0.0)
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 129, in test_a_step_10
    self.assertEqual(expected_output[index], actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1046, in assertTupleEqual
    self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Tuples differ: (0, -1) != (2.0, 0.0)

First differing element 0:
0
2.0

- (0, -1)
+ (2.0, 0.0)
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_m_Vector_1_repr
ERROR: Test case for function: Vector_repr
ERROR: Input: (1, 2, 3)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: <1, 2, 3>
ERROR: '<1, 2, 3>' != '<1,2,3>'
- <1, 2, 3>
?    -  -
+ <1,2,3>

ERROR: ----------------------------------------------------------------------------
ERROR: '<1, 2, 3>' != '<1,2,3>'
- <1, 2, 3>
?    -  -
+ <1,2,3>
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 494, in test_m_Vector_1_repr
    self.assertEqual(expected_output, repr(vector_1))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: '<1, 2, 3>' != '<1,2,3>'
- <1, 2, 3>
?    -  -
+ <1,2,3>

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_m_Vector_1_repr
ERROR: Test case for function: Vector_repr
ERROR: Input: (-1, 0, -3)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: <-1, 0, -3>
ERROR: '<-1, 0, -3>' != '<-1,0,-3>'
- <-1, 0, -3>
?     -  -
+ <-1,0,-3>

ERROR: ----------------------------------------------------------------------------
ERROR: '<-1, 0, -3>' != '<-1,0,-3>'
- <-1, 0, -3>
?     -  -
+ <-1,0,-3>
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 494, in test_m_Vector_1_repr
    self.assertEqual(expected_output, repr(vector_1))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: '<-1, 0, -3>' != '<-1,0,-3>'
- <-1, 0, -3>
?     -  -
+ <-1,0,-3>

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_n_Vector_2_all
ERROR: Test case for function: Vector_all
ERROR: Input: Multiple operations on vectors
ERROR: Actual output: <0,0,0>
ERROR: Expected output: <0, 0, 0>
ERROR: '<0, 0, 0>' != '<0,0,0>'
- <0, 0, 0>
?    -  -
+ <0,0,0>

ERROR: ----------------------------------------------------------------------------
ERROR: '<0, 0, 0>' != '<0,0,0>'
- <0, 0, 0>
?    -  -
+ <0,0,0>
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment8/cl101/a8_hidden_test.py", line 521, in test_n_Vector_2_all
    self.assertEqual("<0, 0, 0>", actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1209, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: '<0, 0, 0>' != '<0,0,0>'
- <0, 0, 0>
?    -  -
+ <0,0,0>

ERROR: ============================================================================
```
```
