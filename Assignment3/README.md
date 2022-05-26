# Assignment 3

- Username: cl101
- Commit hash used for grading: f7083b292981bbe3aaaad8226ebf8200a45b570e

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: _/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (48.17/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `N`: 3.0/3
    - `N_t`: 3.0/3
    - `W`: 3.0/3
    - `L`: 2.0/2
    - TA Comments: TA did not add any comments.

- Problem 2:
    - `q`: 4.0/4
    - TA Comments: TA did not add any comments.

- Problem 3:
    - `amt`: 6.0/6
    - TA Comments: TA did not add any comments.

- Problem 4:
    - `f`: 5.0/5
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `arithmetic_mean`, `geo_mean`, `har_mean`, `RMS_mean`: 6.2/8
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `F`, `V`, `C`: 7.0/7
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `Mortgage`, `total_paid`: 4.0/4
    - TA Comments: TA did not add any comments.


- Problem 8:
    - `is_geo`: 5.0/5
    - TA Comments: TA did not add any comments.



## Code Review & style (_/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to a proper python code.
3. Your logic has to correct.
4. You may pass our test cases but loose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `N`: _/3
    - `N_t`: _/3
    - `W`: _/3
    - `L`: _/2
    - TA Comments: TA did not add any comments.

- Problem 2:
    - `q`: _/4
    - TA Comments: TA did not add any comments.

- Problem 3:
    - `amt`: _/6
    - TA Comments: TA did not add any comments.

- Problem 4:
    - `f`: _/5
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `arithmetic_mean`, `geo_mean`, `har_mean`, `RMS_mean`: _/8
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `F`, `V`, `C`: _/7
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `Mortgage`, `total_paid`: _/4
    - TA Comments: TA did not add any comments.


- Problem 8:
    - `is_geo`: _/5
    - TA Comments: TA did not add any comments.


## Unittest Results
ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/cl101/a3_hidden_test.py", line 249, in test_stats_1_sample_am
    check_assertion(result, self.assertEqual, None, j, a3.arithmetic_mean, i)

ERROR: Input: ([],) -- ignore the outermost () and the trailing ,
ERROR: division by zero
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/cl101/a3_hidden_test.py", line 258, in test_stats_1_sample_gm
    check_assertion(result, self.assertEqual, None, er_msg0, a3.geo_mean, [])

ERROR: Input: ([],) -- ignore the outermost () and the trailing ,
ERROR: division by zero
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/cl101/a3_hidden_test.py", line 275, in test_stats_1_sample_hm
    check_assertion(result, self.assertEqual, None, er_msg1, a3.har_mean, [1,2.3,0,5])

ERROR: Input: ([1, 2.3, 0, 5],) -- ignore the outermost () and the trailing ,
ERROR: division by zero
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/cl101/a3_hidden_test.py", line 276, in test_stats_1_sample_hm
    check_assertion(result, self.assertEqual, None, er_msg0, a3.har_mean, [])

ERROR: Input: ([],) -- ignore the outermost () and the trailing ,
ERROR: division by zero
ERROR: ======================================

ERROR: -------------------------------------
ERROR: Failed test case:   File "/home/sara/Desktop/Spring-2022/Gradingdata/Assignment3/cl101/a3_hidden_test.py", line 285, in test_stats_1_sample_rms
    check_assertion(result, self.assertEqual, None, er_msg0, a3.RMS_mean, [])

ERROR: Input: ([],) -- ignore the outermost () and the trailing ,
ERROR: division by zero
ERROR: ======================================

