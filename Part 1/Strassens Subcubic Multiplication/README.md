# Strassen's Subcubic Matrix Multiplication in Python

## Problem
The conventional matrix multiplication algorithm, using 3 nested for loops, offers a time complexity of O(n<sup>3</sup>).
But, in 1969, a german mathematician, showed that that is not the most optimal solution and came up with his algorithm which,
in my opinion, is oneof the most "non-obvious" solutions to any problem ever. But I do suspect it was somewhat inspired from Karatsuba's Algorithm.
This algorithm, just like all others in this section, takes a divide and conquer approach.

## Pseudo Code
**Input:** _n x n_ integer matrices X and Y.  
**Output: Z = X · Y**  
**Assumption:** n is a power of 2.
```
if n = 1 then // base case
  return the 1 x 1 matrix with entry X[1][1] · Y[1][1]

else // recursive case
  A, B, C, D := submatrices of X as in (3.3)
  E, F, G, H := submatrices of Y as in (3.3)
  recursively compute seven (cleverly chosen) products
  involving A, B,..., H
  return the appropriate (cleverly chosen) additions
  and subtractions of the matrices computed in the
  previous step
```

## Approach
Consider 2 _nxn_ matrices **X** and **Y** to be multiplied.
Now, let **a, b, c, d** be quarters of **X**, and **e, f, g, h** for **Y**.

![X](https://latex.codecogs.com/gif.latex?X%20%3D%20%5Cbegin%7Bpmatrix%7D%20a%20%26%20b%5C%5C%20c%20%26%20d%20%5Cend%7Bpmatrix%7D)  
![Y](https://latex.codecogs.com/gif.latex?Y%20%3D%20%5Cbegin%7Bpmatrix%7D%20e%20%26%20f%5C%5C%20g%20%26%20h%20%5Cend%7Bpmatrix%7D)

Now, thier multiplication can be written as:  

![multip](https://latex.codecogs.com/gif.latex?%5Clarge%20X%20%5Ccdot%20Y%20%3D%20%5Cbegin%7Bpmatrix%7D%20a%20e%20&plus;%20b%20g%20%26%20a%20f%20&plus;%20b%20h%5C%5C%20c%20e%20&plus;%20d%20g%20%26%20c%20f%20&plus;%20d%20h%20%5Cend%7Bpmatrix%7D)

Now, the thing is, we will need 8 recursive calls to execute this equation, which means the recurrence relation will be:  

![recrela1](https://latex.codecogs.com/gif.latex?T%28n%29%20%3D%208%20%5Ccdot%20T%28%5Cfrac%7Bn%7D%7B2%7D%29%20&plus;%20O%28n%5E%7B2%7D%29)

This still gives a running time of **O(n<sup>3</sup>)**
But the genius of Strassen realised that we can get away with just 7 recursive calls with some mathemamagical rearrangement.  

![p1](https://latex.codecogs.com/gif.latex?P_%7B1%7D%20%3D%20a%20%5Ccdot%20%28f%20-%20h%29)  
![p2](https://latex.codecogs.com/gif.latex?P_%7B2%7D%20%3D%20%28a%20&plus;%20b%29%20%5Ccdot%20%28h%29)  
![p3](https://latex.codecogs.com/gif.latex?P_%7B3%7D%20%3D%20%28c%20&plus;%20d%29%20%5Ccdot%20%28e%29)  
![p4](https://latex.codecogs.com/gif.latex?P_%7B4%7D%20%3D%20d%20%5Ccdot%20%28g%20-%20e%29)  
![p5](https://latex.codecogs.com/gif.latex?P_%7B5%7D%20%3D%20%28a%20&plus;%20d%29%20%5Ccdot%20%28e%20&plus;%20h%29)  
![p6](https://latex.codecogs.com/gif.latex?P_%7B6%7D%20%3D%20%28b%20-%20d%29%20%5Ccdot%20%28g%20&plus;%20h%29)  
![p7](https://latex.codecogs.com/gif.latex?P_%7B7%7D%20%3D%20%28a%20-%20c%29%20%5Ccdot%20%28e%20&plus;%20f%29)  

Thus the resulting matix can be obtained by normal addition and subtraction of these 7 products:  

![finalmatrix](https://latex.codecogs.com/gif.latex?%5Clarge%20X%20%5Ccdot%20Y%20%3D%20%5Cbegin%7Bpmatrix%7D%20P_%7B5%7D%20&plus;%20P_%7B4%7D%20-%20P_%7B2%7D%20&plus;%20P_%7B6%7D%20%26%20P_%7B1%7D%20&plus;%20P_%7B2%7D%20%5C%5C%20P_%7B3%7D%20&plus;%20P_%7B4%7D%20%26%20P_%7B1%7D%20&plus;%20P_%7B5%7D%20-%20P_%7B3%7D%20-%20P_%7B7%7D%20%5Cend%7Bpmatrix%7D)

Replacing this, the recurrence relation becomes:  

![recrela2](https://latex.codecogs.com/gif.latex?T%28n%29%20%3D%207%20%5Ccdot%20T%28%5Cfrac%7Bn%7D%7B2%7D%29%20&plus;%20O%28n%5E%7B2%7D%29)

Thus, the overall running time reduces to 

![runningtime](https://latex.codecogs.com/gif.latex?%5Clarge%20O%28n%5E%7B%5Clog%20_%7B2%7D%207%7D%29%20%5Csimeq%20O%28n%5E%7B2.8%7D%29)
