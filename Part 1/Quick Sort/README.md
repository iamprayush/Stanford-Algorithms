# Quick Sort in Python

Here I have chosen the pivot element based on the "median-of-three" method where the median of the left, right and middle elements of
the given subarray is taken. 
The running time of QuickSort highly depends upon the choice of pivot and it can be quadratic
in the worst case (if array is sorted and you take the first element as pivot) or it can be as good as O(nlogn) if a good pivot is chosen.

## Pseudo Code

**Input:** array A of n distinct integers.  
**Output:** array with the same integers, sorted from smallest to largest.

```
Partition(A, l, r)
  pivot := A[l]           // or whatever method you've chosen for pivot
  i := l+1
  for j=l+1 to r
    if A[j] < p           // if A[j] >= pivot, do nothing
      swap A[j] and A[i]
      i++
  swap A[l] and A[i-1]
  
//Then just recursively call Partition on left and right subarrays of the pivot
Partition(A, l, pivotInd-1) // left
Partition(A, pivotInd+1, r) // right
```

## Running Time

**According to the Master Theorem, the recurrence would be:**  

![recurrence relation](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20T%28n%29%20%5Cleq%202%5E%7Bk%7DT%28%5Cfrac%7Bn%7D%7B2%5E%7Bk%7D%7D%29%20&plus;%20kn)

**And the worst case runnning time to be:**

![worstcase](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20O%28n%5E%7B2%7D%29)

**From the recurrence relation we get the average runnning time to be:**

![running time](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20O%28n%5Clog%20n%29)
