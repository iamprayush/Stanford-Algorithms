# Merge Sort in Python

## Pseudo Code

**Input:** array A of n distinct integers.  
**Output:** array with the same integers, sorted from smallest to largest.

```
// ignoring base cases
C := recursively sort first half of A
D := recursively sort second half of A
return Merge (C,D)
```

## Running Time

**According to the Master Theorem, the recurrence would be:**  

![recurrence relation](http://latex.codecogs.com/gif.latex?T%28n%29%20%3D%202%20%5Ccdot%20T%28%20%5Cfrac%7Bn%7D%7B2%7D%20%29%20&plus;%20O%28n%29)

**From the recurrence relation we get the overall runnning time to be:**

![running time](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20O%28n%5Clog%20n%29)
