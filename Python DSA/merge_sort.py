nums = [1,4,5,3,2,5,9,7,5]
def merge_arr(left_arr, right_arr):
    result = []
    i,j = 0,0
    n,m = len(left_arr), len(right_arr)
    while i < n and j < m:
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    if i<n:
        while i < n:
            result.append(left_arr[i])
            i += 1
    if j< m:
        while j<m:
            result.append(right_arr[j])
            j += 1
    return result
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left_half = nums [:mid]
    right_half = nums[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge_arr(left_half,right_half)
result1 = merge_sort(nums)
print(result1)