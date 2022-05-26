# Assignment 2

- Username: cl101
- Commit hash used for grading: 1ae333707907573c5bf9ed961b64974f4677dd05

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 98/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (48/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `g`: 6/10
    - TA Comments: There was an Inscribe post from the professor stating `g(1) = 1` and `g(x) = x + 2 if x != 1`.

- Problem 2:
    - `f`: 10/10
    - TA Comments: Excellent work

- Problem 3:
    - `h_0`: 3/3
    - `h_1`: 3/3
    - `h`: 4/4
    - TA Comments: Excellent work

- Problem 4:
    - `q`: 15/15
    - TA Comments: Excellent work


- Problem 5:
    - `eq`: 20/20
    - TA Comments: Excellent work


- Problem 6:
    - `path`: 20/20
    - TA Comments: Excellent work


- Problem 7:
    - `max2d`: 7/7
    - `max3d`: 8/8
    - TA Comments: Excellent work



## Code Review & style (50/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to a proper python code.
3. Your logic has to correct.
4. You may pass our test cases but loose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

 Problem 1:
    - `g`: 10/10
    - TA Comments: Great job and Excellent code

- Problem 2:
    - `f`: 10/10
    - TA Comments: Great job!

- Problem 3:
    - `h_0`: 3/3
    - `h_1`: 3/3
    - `h`: 4/4
    - TA Comments: Great job!

- Problem 4:
    - `q`: 15/15
    - TA Comments: Great job!


- Problem 5:
    - `eq`: 20/20
    - TA Comments: Great job!


- Problem 6:
    - `path`: 20/20
    - TA Comments: Great job!


- Problem 7:
    - `max2d`: 7/7
    - `max3d`: 8/8
    - TA Comments: Great job!



## Unittest Results
1
2
3.01
error: year
12.0
15
17.6
error: year
32.0
6.708333333333329
3.0
(1.0, -1.0)
(2.5, -2.3333333333333335)
(7.887482193696061, -0.8874821936960613)
True
False
True
True
True
False
3
3
3
3
3
2
-------------------------------------
test_g_4_one failed.

Traceback (most recent call last):
  File "/Users/pradeepreddyrokkam/Desktop/Spring-2022/Gradingdata/Assignment2/cl101/a2_hidden_test.py", line 16, in test_g_4_one
    self.assertAlmostEqual(a2.g(0), 2, 2)
AssertionError: 1 != 2 within 2 places (1 difference)

======================================

1
2
3.01
error: year
12.0
15
17.6
error: year
32.0
6.708333333333329
3.0
(1.0, -1.0)
(2.5, -2.3333333333333335)
(7.887482193696061, -0.8874821936960613)
True
False
True
True
True
False
3
3
3
3
3
2
1
2
3.01
error: year
12.0
15
17.6
error: year
32.0
6.708333333333329
3.0
(1.0, -1.0)
(2.5, -2.3333333333333335)
(7.887482193696061, -0.8874821936960613)
True
False
True
True
True
False
3
3
3
3
3
2
Code tests: 48.0/50.0
g: 6/10
f: 10/10
h0: 3/3
h1: 3/3
h: 4/4
q: 15/15
eq: 20/20
path: 20/20
max2d: 7/7
max3d: 8/8
(base) pradeepreddyrokkam@Pradeeps-MacBook-Air cl101 % 