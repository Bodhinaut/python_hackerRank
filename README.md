# HackerRank Coding Challenges

---
## Solve Algorithms - Algorithms - Warmup
### solveMeFirst
Complete the function solveMeFirst to compute the sum of two integers.

Function prototype:

int solveMeFirst(int x, int y);

where,

x is the first integer input.
y is the second integer input
Return values

sum of the above two integers
Sample Input

x = 2
y = 3
Sample Output
5

---

### simpleArraySum

Given an array of integers, find the sum of its elements.

Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers representing the array's elements.

Output Format

Print the sum of the array's elements as a single integer.

Sample Input

6
1 2 3 4 10 11
Sample Output

31

---

### compare_the_triplets

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison points by comparing  with ,  with , and  with .

If , then Alice is awarded  point.
If , then Bob is awarded  point.
If , then neither person receives a point.
Comparison points is the total points a person earned.

Given  and , can you compare the two challenges and print their respective comparison points?

---


### veryBigSum
Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Input Format

The first line of the input consists of an integer . 
The next line contains  space-separated integers contained in the array.

Output Format

Print the integer sum of the elements in the array

---

### diag_diff
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer,  denoting the number of rows and columns in the matrix . 
The next  lines denote the matrix 's rows, with each line containing  space-separated integers describing the columns.

---

### plus_minus
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.


---

### staircase
Consider a staircase of size :

   #
  ##
 ###
####
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Input Format

A single integer, , denoting the size of the staircase.

Output Format

Print a staircase of size  using # symbols and spaces.

Note: The last line must have  spaces in it.

Sample Input

6 
Sample Output

     #
    ##
   ###
  ####
 #####
######
Explanation

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .
