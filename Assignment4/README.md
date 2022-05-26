# Assignment 4

- Username: cl101
- Commit hash used for grading: 2670d935476f086e45c0952df67c0adf529d1bce

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |


OVERALL: Very good job. You code is very clear and readable, and I like that you keep track of your debugging with comments.

## Total Score: 99.2/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (49.2/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `a`, `b`, `c`, `day`: 9.0/9
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `q`: 8.0/8
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `inner_prod`, `mag`, `angle`, `match`, `best_match`: 9.2/10
    - TA Comments: 
        in the case that thereis only one value of score in the input, your if statement on line 98 never evaluates true, and as a consequence you're returning an empty list in thoes cases. If you change the condition to "<= theta:" it should solve the bug.


- Problem 4:
    - `intersect`: 6.0/6
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `mean`, `variance`, `std`, `mean_centered`: 10.0/10
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `equi`: 7.0/7
    - TA Comments: TA did not add any comments.



## Code Review & style (50/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `a`, `b`, `c`, `day`: _9/9
    - TA Comments: TA did not add any comments.


- Problem 2:
    - `q`: 8/8
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `inner_prod`, `mag`, `angle`, `match`, `best_match`: 10/10
    - TA Comments: TA did not add any comments.



- Problem 4:
    - `intersect`: 6/6
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `mean`, `variance`, `std`, `mean_centered`: 10/10
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `equi`: 7/7
    - TA Comments: TA did not add any comments.


## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_bestmatch_4_end_to_end
ERROR: Input: [[1], [1]]
ERROR: 0 != 3
ERROR: ----------------------------------------------------------------------------
ERROR: 0 != 3
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/Assignment4/cl101/a4_hidden_test.py", line 149, in test_bestmatch_4_end_to_end
    self.assertEqual(len(return_value), 3)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/home/sara/anaconda3/lib/python3.9/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 0 != 3
ERROR: ============================================================================
```
```
