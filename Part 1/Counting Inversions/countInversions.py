def count_split_inversions(left_arr, right_arr):
    li, ri, inversions = 0, 0, 0
    merged = []
    while li < len(left_arr) and ri < len(right_arr):
        if left_arr[li] < right_arr[ri]:
            merged.append(left_arr[li])
            li += 1
        else:
            merged.append(right_arr[ri])
            ri += 1
            inversions += len(left_arr) - li
    for i in range(li, len(left_arr)):
        merged.append(left_arr[i])
    for i in range(ri, len(right_arr)):
        merged.append(right_arr[i])
    return merged, inversions

def count_inversions(arr, l, r):
    if l == r:
        return [arr[l]], 0
    m = (l + r) // 2
    left_arr, left_inversions = count_inversions(arr, l, m)
    right_arr, right_inversions = count_inversions(arr, m + 1, r)
    merged_arr, split_inversions = count_split_inversions(left_arr, right_arr)
    return merged_arr, left_inversions + split_inversions + right_inversions
