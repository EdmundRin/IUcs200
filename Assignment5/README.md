# Assignment 5

- Username: cl101
- Commit hash used for grading: e004bfab7925405fe5d3713c763d1726ff8a7451

- Graded by: Abdul Barr Mohammed

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 90.3/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (45.3/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `makeProbability`:3.0/3
    - `entropy`: 3.0/3
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `L`: 6.0/7
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `div9`: 7.0/7
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `p`:3.0/3
    - `c`:1.5/3
    - `d`: 3.0/3
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `potato`: 4.8/7
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `msi`: 7.0/7
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `dollars`: 7.0/7
    - TA Comments: TA did not add any comments.

## Code Review & style (45/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `makeProbability`: 3/3
    - `entropy`: 3/3
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `L`: 7/7
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `div9`: 7/7
    - TA Comments: TA did not add any comments.


- Problem 4:
    - `p`: 3/3
    - `c`: 2/3
    - `d`: 3/3
    - Did not do one of the c functions 


- Problem 5:
    - `potato`: 3/7
    - Your insertion fuction does not match from lecture and you did not use your insertion function for the potato function


- Problem 6:
    - `msi`: 7/7
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `dollars`: 7/7
    - TA Comments: TA did not add any comments.

## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_L_2_hard
ERROR: Test case for function: L
ERROR: Input: ([0, 0, 0, 0, 0, 0],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 0
ERROR: maximum recursion depth exceeded in comparison
ERROR: ----------------------------------------------------------------------------
ERROR: maximum recursion depth exceeded in comparison
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 74, in check_assertion
    actual_output = function_to_test(*function_params)
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5.py", line 72, in L
    return len(helper(newlist))
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5.py", line 71, in helper
    return helper(xlist)
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5.py", line 71, in helper
    return helper(xlist)
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5.py", line 71, in helper
    return helper(xlist)
  [Previous line repeated 989 more times]
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5.py", line 66, in helper
    for i in max(xlist):
RecursionError: maximum recursion depth exceeded in comparison
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 1
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 9
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 2
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 82
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 3
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 756
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 4
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 7048
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 5
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 66384
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 6
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 631072
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 7
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 6048576
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 8
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 58388608
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 9
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 567108864
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_c_3_hidden
ERROR: Test case for function: c
ERROR: Input: 10
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 5536870912
ERROR: module 'a5' has no attribute 'c_g'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'a5' has no attribute 'c_g'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 257, in test_c_3_hidden
    gen = a5.c_g()
AttributeError: module 'a5' has no attribute 'c_g'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([-3, -4, -2, -1, 0, 1, 2],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [-3, -4, -2, -1, 0, 1, 2]
ERROR: Expected output: [-4, -3, -2, -1, 0, 1, 2]
ERROR: Lists differ: [-4, -3, -2, -1, 0, 1, 2] != [-3, -4, -2, -1, 0, 1, 2]

First differing element 0:
-4
-3

- [-4, -3, -2, -1, 0, 1, 2]
?      ----

+ [-3, -4, -2, -1, 0, 1, 2]
?  ++++

ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [-4, -3, -2, -1, 0, 1, 2] != [-3, -4, -2, -1, 0, 1, 2]

First differing element 0:
-4
-3

- [-4, -3, -2, -1, 0, 1, 2]
?      ----

+ [-3, -4, -2, -1, 0, 1, 2]
?  ++++
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [-4, -3, -2, -1, 0, 1, 2] != [-3, -4, -2, -1, 0, 1, 2]

First differing element 0:
-4
-3

- [-4, -3, -2, -1, 0, 1, 2]
?      ----

+ [-3, -4, -2, -1, 0, 1, 2]
?  ++++

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([-1, -1, -1, -2.0],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [-1, -1, -1, -2.0]
ERROR: Expected output: [-2.0, -1, -1, -1]
ERROR: Lists differ: [-2.0, -1, -1, -1] != [-1, -1, -1, -2.0]

First differing element 0:
-2.0
-1

- [-2.0, -1, -1, -1]
+ [-1, -1, -1, -2.0]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [-2.0, -1, -1, -1] != [-1, -1, -1, -2.0]

First differing element 0:
-2.0
-1

- [-2.0, -1, -1, -1]
+ [-1, -1, -1, -2.0]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [-2.0, -1, -1, -1] != [-1, -1, -1, -2.0]

First differing element 0:
-2.0
-1

- [-2.0, -1, -1, -1]
+ [-1, -1, -1, -2.0]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([5, 4, 3, 2, 7, 6, 8, 9, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [5, 4, 3, 2, 7, 6, 8, 9, 1]
ERROR: Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
ERROR: Lists differ: [1, 2, 3, 4, 5, 6, 7, 8, 9] != [5, 4, 3, 2, 7, 6, 8, 9, 1]

First differing element 0:
1
5

- [1, 2, 3, 4, 5, 6, 7, 8, 9]
+ [5, 4, 3, 2, 7, 6, 8, 9, 1]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5, 6, 7, 8, 9] != [5, 4, 3, 2, 7, 6, 8, 9, 1]

First differing element 0:
1
5

- [1, 2, 3, 4, 5, 6, 7, 8, 9]
+ [5, 4, 3, 2, 7, 6, 8, 9, 1]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5, 6, 7, 8, 9] != [5, 4, 3, 2, 7, 6, 8, 9, 1]

First differing element 0:
1
5

- [1, 2, 3, 4, 5, 6, 7, 8, 9]
+ [5, 4, 3, 2, 7, 6, 8, 9, 1]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([4, 3, 5, 6, 2, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [4, 3, 5, 6, 2, 1]
ERROR: Expected output: [1, 2, 3, 4, 5, 6]
ERROR: Lists differ: [1, 2, 3, 4, 5, 6] != [4, 3, 5, 6, 2, 1]

First differing element 0:
1
4

- [1, 2, 3, 4, 5, 6]
+ [4, 3, 5, 6, 2, 1]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5, 6] != [4, 3, 5, 6, 2, 1]

First differing element 0:
1
4

- [1, 2, 3, 4, 5, 6]
+ [4, 3, 5, 6, 2, 1]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5, 6] != [4, 3, 5, 6, 2, 1]

First differing element 0:
1
4

- [1, 2, 3, 4, 5, 6]
+ [4, 3, 5, 6, 2, 1]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([3, 2, 4, 5, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [3, 2, 4, 5, 1]
ERROR: Expected output: [1, 2, 3, 4, 5]
ERROR: Lists differ: [1, 2, 3, 4, 5] != [3, 2, 4, 5, 1]

First differing element 0:
1
3

- [1, 2, 3, 4, 5]
+ [3, 2, 4, 5, 1]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5] != [3, 2, 4, 5, 1]

First differing element 0:
1
3

- [1, 2, 3, 4, 5]
+ [3, 2, 4, 5, 1]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5] != [3, 2, 4, 5, 1]

First differing element 0:
1
3

- [1, 2, 3, 4, 5]
+ [3, 2, 4, 5, 1]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([3, 2, 4, 5, 1],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [3, 2, 4, 5, 1]
ERROR: Expected output: [1, 2, 3, 4, 5]
ERROR: Lists differ: [1, 2, 3, 4, 5] != [3, 2, 4, 5, 1]

First differing element 0:
1
3

- [1, 2, 3, 4, 5]
+ [3, 2, 4, 5, 1]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 3, 4, 5] != [3, 2, 4, 5, 1]

First differing element 0:
1
3

- [1, 2, 3, 4, 5]
+ [3, 2, 4, 5, 1]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 3, 4, 5] != [3, 2, 4, 5, 1]

First differing element 0:
1
3

- [1, 2, 3, 4, 5]
+ [3, 2, 4, 5, 1]
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([1, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [1, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14]
ERROR: Expected output: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] != [1, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14]

First differing element 4:
6
7

- [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
?                 ---          ----          ----

+ [1, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14]
?              +++        ++++             ++++

ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] != [1, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14]

First differing element 4:
6
7

- [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
?                 ---          ----          ----

+ [1, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14]
?              +++        ++++             ++++
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] != [1, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14]

First differing element 4:
6
7

- [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
?                 ---          ----          ----

+ [1, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14]
?              +++        ++++             ++++

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([1, 4, 2, 9, 5, 7, 6],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [1, 4, 2, 9, 5, 7, 6]
ERROR: Expected output: [1, 2, 4, 5, 6, 7, 9]
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9] != [1, 4, 2, 9, 5, 7, 6]

First differing element 1:
2
4

- [1, 2, 4, 5, 6, 7, 9]
?        ^     ---   ^

+ [1, 4, 2, 9, 5, 7, 6]
?     +++   ^        ^

ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9] != [1, 4, 2, 9, 5, 7, 6]

First differing element 1:
2
4

- [1, 2, 4, 5, 6, 7, 9]
?        ^     ---   ^

+ [1, 4, 2, 9, 5, 7, 6]
?     +++   ^        ^
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 4, 5, 6, 7, 9] != [1, 4, 2, 9, 5, 7, 6]

First differing element 1:
2
4

- [1, 2, 4, 5, 6, 7, 9]
?        ^     ---   ^

+ [1, 4, 2, 9, 5, 7, 6]
?     +++   ^        ^

ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_potato_7
ERROR: Test case for function: potato
ERROR: Input: ([1, 4, 2, 9, 12, 5, 7, 6],) -- ignore the outermost () and the trailing ',' if any
ERROR: Actual output: [1, 4, 2, 9, 12, 5, 7, 6]
ERROR: Expected output: [1, 2, 4, 5, 6, 7, 9, 12]
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9, 12] != [1, 4, 2, 9, 12, 5, 7, 6]

First differing element 1:
2
4

- [1, 2, 4, 5, 6, 7, 9, 12]
+ [1, 4, 2, 9, 12, 5, 7, 6]
ERROR: ----------------------------------------------------------------------------
ERROR: Lists differ: [1, 2, 4, 5, 6, 7, 9, 12] != [1, 4, 2, 9, 12, 5, 7, 6]

First differing element 1:
2
4

- [1, 2, 4, 5, 6, 7, 9, 12]
+ [1, 4, 2, 9, 12, 5, 7, 6]
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment5/cl101/a5_hidden_test.py", line 78, in check_assertion
    assertion(expected_output, actual_output)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1035, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 1017, in assertSequenceEqual
    self.fail(msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 668, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [1, 2, 4, 5, 6, 7, 9, 12] != [1, 4, 2, 9, 12, 5, 7, 6]

First differing element 1:
2
4

- [1, 2, 4, 5, 6, 7, 9, 12]
+ [1, 4, 2, 9, 12, 5, 7, 6]
ERROR: ============================================================================
```
```
