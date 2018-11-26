# Counting Inversions in Python

## Problem:  
**Input:** An array A of distinct integers.  
**Output:** The number of inversions of A—the number of pairs (i, j) of array indices with i<j and A[i] > A[j].

_A naive brute force approach would yield a worst case running time of **O(n<sup>2</sup>)**_  
**But, we can do better!**  
**We will use a divide and conquer approach**

## Pseudo Code
**Input:** array A of n distinct integers.
**Output:** the number of inversions of A.  
```
if n = 0 or n = 1 then // base cases
return 0
else
lef tInv := CountInv(first half of A)
rightInv := CountInv(second half of A)
splitInv := CountSplitInv(A)
return lef tInv + rightInv + splitInv
```
## Running Time

**According to the Master Theorem, the recurrence would be:**  

![recurrence relation](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20T%28n%29%20%3D%202%20%5Ccdot%20T%28%5Cfrac%7Bn%7D%7B2%7D%29%20&plus;%20O%28n%20%5Clog%20n%29)

**From the recurrence relation we get the overall runnning time to be:**

![running time](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20O%28n%20%5Ccdot%20%5Clog%20n%29)
