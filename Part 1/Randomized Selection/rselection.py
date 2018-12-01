# Version 3.6

import random

arr = [10, 8, 2, 4]
k = 3                # The statistic (kth lowest number)(1-based indexed)
# Output should be 8 in this case

def partition(a, left, right):
    """
    Swaps elemnts untill the pivot is in the ideal place.
    Takes O(n) time.
    i represents index at which partition occured.
    a[i] is the leftmost element of the subarray containing elements > than pivot
    Input: array to be sorted, left index of subarray, right index of subarray
    Output: Index of pivot
    """

    # Choosing pivot randomly
    pivot = random.choice(a[left:right+1])

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
      
def randSelection(a, left=0, right=None):
    """
    Uses the same logic as QuickSort, the only diff being that we only recur down one subarray.
    Input: array to be sorted, left index of subarray, right index of subarray
    Output: Value of the kth statistic
    """
    global k
    if not(0 <= k <= len(a)):
        return "Statistic Index out of range!"  # Check if k is in range of array indices

    if right == None:
        right = len(a)-1                        # if we are in the first call of recursion

    # Recursively partition left or right subarrays of the pivot based on the pivot index.
    pivInd = partition(a, left, right)
    if pivInd == k-1:
        return a[pivInd]
    elif pivInd > k-1:
        return randSelection(a, left, pivInd-1)         # left half
    else:
        return randSelection(a, pivInd+1, right)        # right half

print(randSelection(arr))
