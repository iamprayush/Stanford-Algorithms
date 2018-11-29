# Version 3.6

from random import randint

def medianOf3(a, left, right):
    """
    Chooses the median element out of the left, right and middle elements of the given subarray
    Returns the value of the pivot element that ought to be chosen
    """
    return sorted([a[left], a[right], a[(left+right)//2]])[1]

def partition(a, left, right):
    """
    Swaps elemnts untill the pivot is in the ideal place.
    Takes O(n) time.
    i represents index at which partition occured.
    a[i] is the leftmost element of the subarray containing elements > than pivot
    Input: array to be sorted, left index of subarray, right index of subarray
    Output: Index of pivot
    """

    # Choosing pivot by method of 'median-of-three'
    pivot = medianOf3(a, left, right)
    # Swapping the chosen pivot to the left index
    a[a.index(pivot)], a[left] = a[left], a[a.index(pivot)]

    # Partition and swaps
    i = left + 1
    for j in range(left+1, right+1):    # from left+1 of array to right of array
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]     # swapping smaller element with the leftmost element of larger array
            i += 1                      # incrementing partition index
            
    # swapping pivot with rightmost element of the smaller subarray
    a[left], a[i-1] = a[i-1], a[left]
    
    return i-1                          # index of pivot
      
def quicksort(a, left=0, right=None):
    """
    Recursively divides and sorts subarrays
    Inplace sorting so returns nothing, just sorts the given array inplace
    """
    if right == None:
        right = len(a)-1                 # if we are in the first call of recursion

    # Base case when pivot is ideally placed
    if left >= right:
        return                           # Backtracking

    # else recursively partition left and right subarrays of the pivot
    pivInd = partition(a, left, right)
    quicksort(a, left, pivInd-1)         # left half
    quicksort(a, pivInd+1, right)        # right half
