# Midterm Programming Exam

- Username: cl101
- Commit hash used for grading: 50a67c5683b73c6b9ac38fd5247c5f92f277e787

- Graded by: Zach Graber

Rubric:

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 30         |
| Code Review   | 30         |



## Total Score: 60/60
- Please double-check that your Canvas score reflects what is shown here. 
- The programming section of the midterm has 60% of the total grade. The remaining 40% is for the quiz that you took on Canvas. 

## General Comment
- (+1) I'm impressed with your attention to detail in this! For example, you've taken the time to annotate the file, **test your code** (you'd be surprised by how few people did this), and try to account for edge cases like a distance of 0 in the gravity problem. Keep up the good work like this, and you have a really bright future ahead of you in programming!

## Code Tests (29.0/30 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `f`: 10.0/10
    - TA Comments: Nice work!


- Problem 2:
    - `gravity`: 10.0/10
    - TA Comments: TA did not add any comments.


- Problem 3:
    - `tip_amt`: 9.0/10
    - TA Comments: The only issue here is that in your solution, `tip` is defined *inside* the function, whereas the starter code has it outside. This is a subtle yet important difference; when it's outside of the function, `tip` is a global variable, meaning that it can be shared and accessed in any scope (not just inside the function). For example, if you had another function or code snippet that depended on `tip`, it wouldn't be able to find it.



## Code Review & style (30/30 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to be a proper python code.
3. Your logic has to be correct.
4. You may pass our test cases but lose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `f`: 10/10
    - TA Comments: Great heavens! This is some of the neatest, most organized code that I've seen all semester. As a general comment, your variable names are descriptive and you've taken the time to label all the sections of the file, which is **much** appreciated.


- Problem 2:
    - `gravity`: 10/10
    - TA Comments: Wow! I'm impressed that you took the time to consider what would happen if `d == 0`! Nice!


- Problem 3:
    - `tip_amt`: 10/10
    - TA Comments: `tip` inside the function, when it should be outside, but otherwise... great!



## Unittest Results
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_changed_dict
ERROR: Test case for function: tip_amt
ERROR: Input: (100, 'great', 0)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 100.0
ERROR: module 'midterm' has no attribute 'tip'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'midterm' has no attribute 'tip'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/cl101/midterm_tests.py", line 262, in test_tipamt_1_changed_dict
    with mock.patch.dict(midterm.tip, {input[1]: input[2]}):
AttributeError: module 'midterm' has no attribute 'tip'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_changed_dict
ERROR: Test case for function: tip_amt
ERROR: Input: (40, 'bad', 10)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 44.0
ERROR: module 'midterm' has no attribute 'tip'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'midterm' has no attribute 'tip'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/cl101/midterm_tests.py", line 262, in test_tipamt_1_changed_dict
    with mock.patch.dict(midterm.tip, {input[1]: input[2]}):
AttributeError: module 'midterm' has no attribute 'tip'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_changed_dict
ERROR: Test case for function: tip_amt
ERROR: Input: (50, 'good', 15)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 57.5
ERROR: module 'midterm' has no attribute 'tip'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'midterm' has no attribute 'tip'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/cl101/midterm_tests.py", line 262, in test_tipamt_1_changed_dict
    with mock.patch.dict(midterm.tip, {input[1]: input[2]}):
AttributeError: module 'midterm' has no attribute 'tip'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_changed_dict
ERROR: Test case for function: tip_amt
ERROR: Input: (1, 'great', 100)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 2
ERROR: module 'midterm' has no attribute 'tip'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'midterm' has no attribute 'tip'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/cl101/midterm_tests.py", line 262, in test_tipamt_1_changed_dict
    with mock.patch.dict(midterm.tip, {input[1]: input[2]}):
AttributeError: module 'midterm' has no attribute 'tip'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_changed_dict
ERROR: Test case for function: tip_amt
ERROR: Input: (1, 'good', 1)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 1.01
ERROR: module 'midterm' has no attribute 'tip'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'midterm' has no attribute 'tip'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/cl101/midterm_tests.py", line 262, in test_tipamt_1_changed_dict
    with mock.patch.dict(midterm.tip, {input[1]: input[2]}):
AttributeError: module 'midterm' has no attribute 'tip'
ERROR: ============================================================================
```
```
ERROR: ============================================================================
ERROR: Failed test case: test_tipamt_1_changed_dict
ERROR: Test case for function: tip_amt
ERROR: Input: (1, 'bad', 1)
ERROR: Actual output: Function did not execute or function return value could not be captured
ERROR: Expected output: 1.01
ERROR: module 'midterm' has no attribute 'tip'
ERROR: ----------------------------------------------------------------------------
ERROR: module 'midterm' has no attribute 'tip'
Traceback (most recent call last):
  File "/home/sara/Spring-2022/Gradingdata/midterm/cl101/midterm_tests.py", line 262, in test_tipamt_1_changed_dict
    with mock.patch.dict(midterm.tip, {input[1]: input[2]}):
AttributeError: module 'midterm' has no attribute 'tip'
ERROR: ============================================================================
```
```
