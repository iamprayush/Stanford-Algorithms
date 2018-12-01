# Randomized Selection in Python

## Problem:  
**Input:** An array A of distinct integers.  
**Output:** The kth smallest element of the array.  

_A naive brute force approach would yield a worst case running time of **O(n<sup>2</sup>)**_  
_Even a little cheekier sort and return index approach would give **O(nlogn)** running  time_  
**But, we can do better!**  
**We will use a divide and conquer approach, which is based on the logic of QuickSort**  
The main idea here is, after choosing the pivot randomly and going through the partition phase, we check if the 
current pivot index is equal to the desired k statistic in which case we return the value at that index or else
we simply recur down the left or right subarray based on if k < or > current pivot index, respectively.

## Pseudo Code
**Input:** array A of n distinct integers.
**Output:** Value of the kth statistic.  
```
Partition(A, l, r)
// Exactly same as in QuickSort

//Then just recursively call Partition on left or right subarrays of the pivot
if pivInd == k
  return a[pivInd]
else if pivInd > k
  Partition(A, l, pivotInd-1) // left
else
  Partition(A, pivotInd+1, r) // right
```
## Running Time

Here instead of the 2 recursive calls like in QuickSort, we only recur down one of the subarrays.  
**According to the Master Theorem, the recurrence would be:** 

![recurrence relation](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20T%28n%29%20%5Cleq%20T%28%5Cfrac%7Bn%7D%7B2%7D%29%20&plus;%20O%28n%29)

**From the recurrence relation we get the overall runnning time to be:**

![running time](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20O%28n%29)
